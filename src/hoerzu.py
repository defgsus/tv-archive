import json
import datetime
import re
import sys
import traceback
import urllib.parse

import requests

from .util import printe, to_soup
from .scraper import Program, Error, ScraperCallback


BASE_URL = "https://www.hoerzu.de"
_RE_TIME_RANGE = re.compile(r"(\d+):(\d+)\s+bis\s+(\d+):(\d+)")
_RE_BID = re.compile(r".*bid_(\d+).*")
_RE_STAFFEL = re.compile(r".*\(Staffel: (\d+) \| Folge: (\d+)\).*")


def scrape_hoerzu(
        callback: ScraperCallback,
        future_days: int = 0,
):
    session = requests.Session()
    session.headers.update({
        "Referer": f"{BASE_URL}/tv-programm/",
        "Host": "www.hoerzu.de",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
    })

    scrape_hoerzu_overview(session, callback, f"{BASE_URL}/tv-programm/")

    if future_days:
        # TODO: the website does not really work that way
        #   they only provide the overview for the future day
        #   but there seems to be no complete page-per-channel for future days
        today = datetime.date.today()
        for i in range(1, future_days + 1):
            date = today + datetime.timedelta(days=i)
            url = f"{BASE_URL}/tv-programm/{date.strftime('%d.%m.%Y')}/"
            scrape_hoerzu_overview(session, callback, url)


def scrape_hoerzu_overview(session: requests.Session, callback: ScraperCallback, url: str):
    markups = [
        session.get(url).text
    ]

    response = session.get(
        f"{url}?getAdditionalPages=true",
    )
    markups.extend(response.json()["data"])

    for markup in markups:
        soup = to_soup(markup)

        for channel_a in soup.find_all("a", {"class": "m-epg-card__channel-logo"}):
            channel_url = urllib.parse.urljoin(BASE_URL, channel_a.attrs["href"])
            channel_name = channel_a.attrs["title"]

            printe("hoerzu.de:", channel_name, channel_url)

            try:
                _scrape_hoerzu_channel(callback, session, channel_url, channel_name)

            except KeyboardInterrupt:
                return

            except:
                printe(f"EXCEPTION in {channel_url}")
                traceback.print_exc(file=sys.stderr)
                callback(Error(type="channel", url=channel_url))


def _scrape_hoerzu_channel(
        callback: ScraperCallback,
        session: requests.Session,
        channel_url: str,
        channel_name: str,
):
    response = session.get(channel_url)
    soup = to_soup(response.text)

    table_div = soup.find("div", {"class": "m-table__main-table"})
    if not table_div:
        printe(f"No program on {channel_url} ({channel_name})")
        return

    #date_str = table_div.find("h2", {"class": "a-headline"}).text.strip()
    #date = datetime.datetime.strptime(date_str, "%d.%m.%y")

    for tr in table_div.find("tbody").find_all("tr"):
        td = tr.find("td", {"class": "m-table__series-label"})
        if not td:
            continue

        a = td.find("a")
        program_url = urllib.parse.urljoin(BASE_URL, a.attrs["href"])
        program_id = _RE_BID.match(program_url).groups()[0]
        program_name = a.find("strong").text.strip()
        program_subtext = a.find("small").text.strip()

        program_season, program_episode = None, None
        match = _RE_STAFFEL.match(program_subtext)
        if match:
            program_season, program_episode = [int(g.lstrip("0") or "0") for g in match.groups()]
            program_subtext = program_subtext[program_subtext.index(")") + 1:].strip()


        date_str = tr.find("td", {"class": "m-table__date-label"}).text.strip()
        date_str = date_str.split(",")[-1].strip()
        date = datetime.datetime.strptime(date_str, "%d.%m.%Y")

        time_str = tr.find("td", {"class": "m-table__time-label"}).text.strip().replace("\n", " ")
        match = _RE_TIME_RANGE.match(time_str)
        groups = match.groups()

        date_start = date.replace(hour=int(groups[0].lstrip("0") or "0"), minute=int(groups[1].lstrip("0") or "0"))
        date_end = date.replace(hour=int(groups[2].lstrip("0") or "0"), minute=int(groups[3].lstrip("0") or "0"))
        while date_end < date_start:
            date_end += datetime.timedelta(days=1)

        try:
            extra_info = _scrape_hoerzu_program(session, program_url)

            if extra_info.get("countries"):
                for country in reversed(extra_info["countries"]):
                    if not program_subtext.endswith(country):
                        break
                    program_subtext = program_subtext[:-len(country)].rstrip(", ")

        except KeyboardInterrupt:
            raise

        except:
            printe(f"EXCEPTION IN {channel_name}: {program_url}")
            traceback.print_exc(file=sys.stderr)
            callback(Error(type="program-details", url=program_url))
            extra_info = {}

        callback(Program(
            id=program_id,
            url=program_url,
            channel=channel_name,
            title=program_name,
            sub_title=program_subtext,
            date=date_start,
            length=int((date_end - date_start).total_seconds() // 60),
            season=program_season,
            episode=program_episode,
            **extra_info,
        ))


def _scrape_hoerzu_program(
        session: requests.Session,
        program_url: str,
) -> dict:
    response = session.get(program_url)
    soup = to_soup(response.text)

    div = soup.find("div", {"class": "o-epg_stage__header"})

    # title = div.find("h1").text.strip()
    info_str = div.find("div", {"class": "o-epg_stage__series-info"}).text.strip()
    infos = [i.strip() for i in info_str.split("•")]
    try:
        year = int(infos[1][-4:])
        countries = infos[1][:-4]
    except:
        year = None
        countries = infos[1]

    countries = [c.strip() for c in countries.split(",")]

    description = None
    div = soup.find("div", {"class": "p-epg-modal__description"})
    if div:
        description = div.text.strip()

    return {
        "genre": infos[0],
        "year": year,
        "countries": countries,
        "description": description,
    }
