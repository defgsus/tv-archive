import datetime
import json
from typing import Generator

from . import PROJECT_PATH, DATA_PATH
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


def iter_programs_through_commits() -> Generator[Program, None, None]:
    """
    Iterates through all recorded programs, even the ones that are
    overwritten in a subsequent commit.

    Requires "giterator":

        pip install git+https://github.com/defgsus/giterator

    """
    from giterator import Giterator

    filenames = sorted(DATA_PATH.rglob("*.ndjson"))
    giterator = Giterator(PROJECT_PATH)

    id_set = set()
    for filename in filenames:
        rel_filename = str(filename.relative_to(PROJECT_PATH))
        for commit in giterator.iter_commits(rel_filename):
            for file in commit.iter_files(rel_filename):
                for line in file.text().splitlines():
                    program = Program(**json.loads(line))
                    if program.id not in id_set:
                        id_set.add(program.id)

                        program.date = datetime.datetime.strptime(program.date, "%Y-%m-%dT%H:%M:%S")

                        yield program

