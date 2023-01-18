import argparse
import datetime
from src.scraper import Scraper
from src.hoerzu import scrape_hoerzu
from src.util import printe


today = datetime.date.today()
DEFAULT_OUTPUT = f"docs/data/{today.year:04}/{today.month:02}/{today.strftime('%Y-%m-%d')}.ndjson"


def parse_args() -> dict:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "command", type=str,
        choices=["scrape"],
    )
    parser.add_argument(
        "-o", "--output", type=str, nargs="?", default=DEFAULT_OUTPUT,
        help=f"Name of the json output file, default is {DEFAULT_OUTPUT}"
    )
    return vars(parser.parse_args())


def main(command: str, output: str):
    if command == "scrape":
        with Scraper(output_filename=output) as scraper:

            scraper.scrape(scrape_hoerzu)
            print(scraper.commit_message())

    else:
        printe(f"Invalid command '{command}'")
        exit(1)


if __name__ == "__main__":
    main(**parse_args())


