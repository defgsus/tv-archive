import datetime
import json
import os
from pathlib import Path
from dataclasses import dataclass
from typing import Callable, Optional, List, IO, Union, Any


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
    description: Optional[str] = None
    season: Optional[int] = None
    episode: Optional[int] = None
    year: Optional[int] = None
    countries: Optional[List[str]] = None


@dataclass
class Error:
    type: str
    url: str


ScraperCallback = Callable[[Union[Program, Error]], None]


class Scraper:

    def __init__(self, output_filename: Union[str, Path]):
        self.output_filename = Path(output_filename)
        self.output_file: Optional[IO[str]] = None
        self._error_count = {}
        self._channel_count = {}

    def __enter__(self):
        os.makedirs(self.output_filename.parent, exist_ok=True)
        self.output_file = open(self.output_filename, "wt")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.output_file.close()
        self.output_file = None

    def scrape(self, scraper: Callable[[ScraperCallback], None]):
        scraper(self._callback)

    def _callback(self, program: Union[Program, Error]):
        if isinstance(program, Program):
            dump = json.dumps(vars(program), ensure_ascii=False, cls=_JsonEncoder)
            self.output_file.write(dump + "\n")

            if program.channel not in self._channel_count:
                self._channel_count[program.channel] = 0
            self._channel_count[program.channel] += 1

        else:
            if program.type not in self._error_count:
                self._error_count[program.type] = 0
            self._error_count[program.type] += 1

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
