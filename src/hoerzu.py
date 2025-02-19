import json
import datetime
import re
import sys
import traceback
import urllib.parse
from functools import partial
from multiprocessing.pool import ThreadPool
from typing import Optional, Union, List, Tuple

import requests
import bs4

from .util import printe, to_soup
from .scraper import Program, Error, ScraperCallback


class HoerzuScraper:
    BASE_URL = "https://www.hoerzu.de"
    USER_AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/113.0"

    RE_TIME_RANGE = re.compile(r"(\d+):(\d+)\s+bis\s+(\d+):(\d+)")
    RE_BID = re.compile(r".*bid_(\d+).*")
    RE_YEAR = re.compile(r".*(\d\d\d\d)")
    RE_SEASON = re.compile(r"Staffel\s+(\d+)")
    RE_EPISODE = re.compile(r"Folge\s+(\d+)")

    def __init__(self, num_threads: int = 1):
        self.num_threads = num_threads
        self.session = requests.Session()
        self.session.headers.update({
            "Host": self.BASE_URL.split("//")[-1],
            "User-Agent": self.USER_AGENT,
        })

    def scrape(self, callback: ScraperCallback):
        self.callback = callback
        channels = self.get_channels()

        if self.num_threads <= 1:
            for name, url in channels:
                self.scrape_channel(name, url)
        else:
            pool = ThreadPool(8)
            pool.map(lambda t: self.scrape_channel(*t), channels)

    def request(
            self,
            url_path: str,
            params: Optional[dict] = None,
            referer: Optional[str] = None,
    ):
        url = f"{self.BASE_URL}/{url_path.lstrip('/')}"
        return self.session.get(
            url,
            params=params,
            headers={
                "Referer": referer or url,
            }
        )

    def get_soup(
            self,
            url: str,
            params: Optional[dict] = None,
            with_text: bool = False,
    ) -> Union[bs4.BeautifulSoup, Tuple[bs4.BeautifulSoup, str]]:
        response = self.request(url, params=params)
        # need lxml parser because the html dom is buggy ;)
        soup = bs4.BeautifulSoup(response.text, features="lxml")
        return (soup, response.text) if with_text else soup

    def get_channels(self) -> List[Tuple[str, str]]:
        """Get (name, url) tuples"""
        soup = self.get_soup("tv-programm/daserste/")
        div = soup.find("div", {"class": "o-sender-filter__channel-dropdown-list"})
        channels = []
        for a in div.find_all("a"):
            name = a.attrs["data-name"]
            url = a.attrs["href"]
            channels.append((name, url))
        return channels

    def scrape_channel(self, channel_name: str, url: str):
        #soup = self.get_soup(url)
        # instead of channel url^ we request the ajax (html) api
        # to start at an early time
        channel_code = url.rstrip("/").split("/")[-1]
        response = self.request(
            "ajax/sender-tv-json/",
            params={
                "channel": channel_code,
                "channelGroup": "default",
                "date": "heute",
                "time": "05:00",
                "initial": "true",
            },
            referer=f"{self.BASE_URL}/{url.lstrip('/')}"
        )
        soup = to_soup(response.json()["data"])
        date_str = soup.find("span", {"class": "m-table__date"}).text.strip()
        date_str = date_str.split(",")[-1].strip()
        date = datetime.datetime.strptime(date_str, "%d.%m.%Y")

        first_program_date = None
        for tr in soup.find_all("tr", {"class": "sender-table-item"}):
            a = tr.find("a", {"class": "row-link"})
            program_url = a.attrs["href"]
            program_id = self.RE_BID.match(program_url).groups()[0]
            time_str = a.text.strip()

            match = self.RE_TIME_RANGE.match(time_str)
            groups = match.groups()

            date_start = date.replace(
                hour=int(groups[0].lstrip("0") or "0"),
                minute=int(groups[1].lstrip("0") or "0"),
            )
            date_end = date.replace(
                hour=int(groups[2].lstrip("0") or "0"),
                minute=int(groups[3].lstrip("0") or "0"),
            )
            while date_end < date_start:
                date_end += datetime.timedelta(days=1)

            if first_program_date is None:
                first_program_date = date_start

            else:
                while date_start < first_program_date:
                    date_start += datetime.timedelta(days=1)
                    date_end += datetime.timedelta(days=1)

            td = tr.find("td", {"class": "m-table__series-label"})
            title = td.find("a").attrs["title"]
            sub_texts = td.find("a").find("small").text.strip().split("•")

            td = tr.find("td", {"class": "m-table__genre"})
            genre = td.text.strip()

            try:
                extra_info = self.scrape_program(program_url)
            except Exception as e:
                print(f"EXCEPTION: {program_url}, {type(e).__name__}: {e}")
                extra_info = {}

            self.callback(Program(
                id=program_id,
                url=url,
                channel=channel_name,
                title=title,
                date=date_start,
                length=int((date_end - date_start).total_seconds() / 60),
                genre=genre,
                sub_genre=sub_texts[0].strip(),
                countries=[c.strip() for c in sub_texts[1].split(",")],
                **extra_info,
            ))

    def scrape_program(self, url: str) -> dict:
        soup, markup = self.get_soup(url, with_text=True, params={"type": "modal"})
        extra_data = {}

        div = soup.find("div", {"class": "p-epg-modal uk-modal-dialog"})
        if div:
            extra_data["genres"] = div.attrs["data-genres"].split(",")

        infos = soup.find("div", {"class": "o-epg_stage__series-info"}).text.split("•")
        year_match = self.RE_YEAR.match(infos[1].strip())
        if year_match:
            extra_data["year"] = int(year_match.groups()[0])

        h3 = soup.find("h3", {"class": "p-epg-modal__descriptionSubHeadline"})
        if h3:
            h_texts = h3.text.split(",", 2)
            while h_texts:
                h_text = h_texts.pop(0).strip()
                if match := self.RE_SEASON.match(h_text):
                    extra_data["season"] = int(match.groups()[0])
                elif match := self.RE_EPISODE.match(h_text):
                    extra_data["episode"] = int(match.groups()[0])
                else:
                    extra_data["sub_title"] = h_text

        extra_data["description"] = soup.find("div", {"class": "p-epg-modal__description"}).text.strip() or None
        return extra_data
