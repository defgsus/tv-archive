import sys

from bs4 import BeautifulSoup


def printe(*args, **kwargs):
    kwargs["file"] = sys.stderr
    kwargs["flush"] = True
    print(*args, **kwargs)


def to_soup(markup: str) -> BeautifulSoup:
    return BeautifulSoup(markup, features="lxml")
