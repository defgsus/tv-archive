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


ScraperCallback = Callable[[Program], None]


class Scraper:

    def __init__(self, output_filename: Union[str, Path]):
        self.output_filename = Path(output_filename)
        self.output_file: Optional[IO[str]] = None

    def __enter__(self):
        os.makedirs(self.output_filename.parent, exist_ok=True)
        self.output_file = open(self.output_filename, "wt")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.output_file.close()
        self.output_file = None

    def scrape(self, scraper: Callable[[ScraperCallback], None]):
        scraper(self._callback)

    def _callback(self, program: Program):
        dump = json.dumps(vars(program), ensure_ascii=False, cls=_JsonEncoder)
        self.output_file.write(dump + "\n")


class _JsonEncoder(json.JSONEncoder):

    def default(self, o: Any) -> Any:
        if isinstance(o, datetime.datetime):
            return o.isoformat()

        return super().default(o)
