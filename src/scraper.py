import datetime
import json
import os
import re
from copy import copy
from pathlib import Path
from dataclasses import dataclass
from threading import Lock
from typing import Callable, Optional, List, IO, Union, Any, Dict

from . import DATA_PATH
from .util import printe
from .cleaner import cleaned_program


_UPDATED_SCRAPER_DATE = datetime.datetime(2025, 2, 19)


@dataclass
class Program:
    id: str
    url: str
    channel: str
    title: str
    date: datetime.datetime
    length: int  # minutes
    sub_title: Optional[str] = None
    genre: Optional[str] = None
    sub_genre: Optional[str] = None
    genres: Optional[List[str]] = None
    description: Optional[str] = None
    season: Optional[int] = None
    episode: Optional[int] = None
    year: Optional[int] = None
    countries: Optional[List[str]] = None

    def cleaned(self) -> "Program":
        """
        Applies some fixes to individual fields that happened when scraping the program.

        It's a heuristic approach but better than nothing. I encourage to use this
        before calculating any metrics.

        :return: new Program instance
        """
        return cleaned_program(self)


@dataclass
class Error:
    type: str
    url: str


ScraperCallback = Callable[[Union[Program, Error]], None]


class Scraper:

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.output_files: Dict[datetime.date, IO[str]] = {}
        self._error_count = {}
        self._channel_count = {}
        self._file_date = None
        self._lock = Lock()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for fp in self.output_files.values():
            fp.close()
        self.output_files = {}

    def scrape(self, scraper: Callable[[ScraperCallback], None]):
        scraper(self._callback)

    def _callback(self, program: Union[Program, Error]):
        with self._lock:
            if isinstance(program, Program):
                if self.verbose:
                    printe(
                        f"{program.date} {program.channel:20} {program.length}m {program.title}"
                    )
                self._store_program(program)

                if program.channel not in self._channel_count:
                    self._channel_count[program.channel] = 0
                self._channel_count[program.channel] += 1

            else:
                if program.type not in self._error_count:
                    self._error_count[program.type] = 0
                self._error_count[program.type] += 1

    def _store_program(self, program: Program):
        # since 2023-02-19, we always store into ONE ndjson file
        # otherwise one needs to go through the git history to collect
        # programs played at night (0:00 - 5:00)
        if self._file_date is None:
            self._file_date = program.date.date()
        date = self._file_date
        if date not in self.output_files:
            filename = DATA_PATH / f"{date.year:04}" / f"{date.month:02}" / f"{date.strftime('%Y-%m-%d')}.ndjson"
            os.makedirs(filename.parent, exist_ok=True)
            self.output_files[date] = open(filename, "wt")

        dump = json.dumps(vars(program), ensure_ascii=False, cls=_JsonEncoder)
        self.output_files[date].write(dump + "\n")

    def commit_message(self) -> str:
        msg = f"update at {datetime.datetime.utcnow().isoformat()} UTC"

        if self._error_count:
            msg += "\n\n### ERRORS\n\n"
            for key in sorted(self._error_count):
                msg += f"{key}: {self._error_count[key]}\n"

        if self._channel_count:
            msg += "\n\n### programs per channel\n\n"
            max_length = max(len(c) for c in self._channel_count) + 1
            for key in sorted(self._channel_count):
                channel = f"{key}:"
                msg += f"{channel:{max_length}} {self._channel_count[key]}\n"

        return msg


class _JsonEncoder(json.JSONEncoder):

    def default(self, o: Any) -> Any:
        if isinstance(o, datetime.datetime):
            return o.isoformat()

        return super().default(o)
