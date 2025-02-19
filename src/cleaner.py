import datetime
import re
from copy import copy


_UPDATED_SCRAPER_DATE = datetime.datetime(2025, 2, 19)
_RE_FOLGE = re.compile(r"\(\s*Folge:\s+(\d+)\s*\)(.*)")
_RE_STAFFEL = re.compile(r"\(\s*Staffel:\s+(\d+)\s*\|?\s*\)(.*)")
_RE_STAFFEL_FOLGE = re.compile(r"\(\s*Staffel:\s+(\d+)\s+\|\s+Folge:\s+(\d+)\s*\)(.*)")


def cleaned_program(self):
    """
    Applies some fixes to individual fields that happened when scraping the program.

    It's a heuristic approach but better than nothing. I encourage to use this
    before calculating any metrics.

    :return: new Program instance
    """
    prog = copy(self)

    if prog.countries == [""]:
        prog.countries = None

    if prog.genres == [""]:
        prog.genres = None

    if isinstance(prog.date, str):
        prog.date = datetime.datetime.strptime(prog.date, "%Y-%m-%dT%H:%M:%S")

    def _assign_genre(genre: str):
        genre = genre.strip()
        # sometimes, the countries are attached
        if " " in genre and genre not in ("Formel E", ):
            parts = genre.split(maxsplit=1)
            countries = [c.strip() for c in parts[1].split(",")]
            if all(c.isupper() and len(c) <= 3 for c in countries):
                if not prog.countries:
                    prog.countries = countries
                genre = parts[0]

        if not prog.sub_genre and prog.genre:
            prog.sub_genre = prog.genre
            prog.genre = genre
        elif not prog.genre:
            prog.genre = genre
        elif not prog.sub_genre:
            prog.sub_genre = genre

    if prog.sub_title:
        if match := _RE_FOLGE.match(prog.sub_title):
            prog.episode = int(match.groups()[0])
            _assign_genre(match.groups()[1])
            prog.sub_title = None
        elif match := _RE_STAFFEL.match(prog.sub_title):
            prog.season = int(match.groups()[0])
            _assign_genre(match.groups()[1])
            prog.sub_title = None
        elif match := _RE_STAFFEL_FOLGE.match(prog.sub_title):
            prog.season = int(match.groups()[0])
            prog.episode = int(match.groups()[1])
            _assign_genre(match.groups()[2])
            prog.sub_title = None

    # sub_titles were actually genres before that date
    if prog.date < _UPDATED_SCRAPER_DATE and prog.sub_title:
        _assign_genre(prog.sub_title)
        prog.sub_title = None

    for key in ("sub_title", "genre", "sub_genre", "description"):
        if getattr(prog, key) == "":
            setattr(prog, key, None)

    return prog
