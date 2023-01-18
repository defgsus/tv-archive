import datetime
import json
from typing import Generator

from . import DATA_PATH
from .scraper import Program


def iter_programs(

) -> Generator[Program, None, None]:

    filenames = sorted(DATA_PATH.rglob("*.ndjson"))

    for filename in filenames:
        with open(filename, "rt") as fp:
            for line in fp.readlines():
                program = Program(**json.loads(line))

                program.date = datetime.datetime.strptime(program.date, "%Y-%m-%dT%H:%M:%S")

                yield program


