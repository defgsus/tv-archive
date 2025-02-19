import argparse
import datetime

from tqdm import tqdm

from src import DATA_PATH, PROJECT_PATH
from src.scraper import Scraper
from src.hoerzu import HoerzuScraper
from src.util import printe
from src.access import iter_programs


def parse_args() -> dict:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "command", type=str,
        choices=["scrape", "stats", "write-stats"],
    )
    parser.add_argument(
        "-j", "--threads", type=int, default=1,
    )
    parser.add_argument(
        "-v", "--verbose", type=bool, nargs="?", default=False, const=True,
    )
    return vars(parser.parse_args())


def main(command: str, verbose: bool, threads: int):
    if command == "scrape":
        with Scraper(verbose=verbose) as scraper:

            hoerzu = HoerzuScraper(num_threads=threads)
            scraper.scrape(hoerzu.scrape)
            print(scraper.commit_message())

    elif command == "stats":
        print(create_stats_str(verbose=verbose))

    elif command == "write-stats":
        write_stats(verbose=verbose)

    else:
        printe(f"Invalid command '{command}'")
        exit(1)


def create_stats_str(verbose: bool = False) -> str:
    top_count = 30

    channel_set = set()
    genre_counter = {}
    all_play_time = 0
    num_programs = 0
    date_min, date_max = None, None
    # from src.access import iter_programs_through_commits as iter_programs
    for program in tqdm(iter_programs(), disable=not verbose):
        num_programs += 1
        key = program.genre or "*unknown*"
        all_play_time += program.length
        genre_counter[key] = genre_counter.get(key, 0) + program.length

        if date_min is None or program.date < date_min:
            date_min = program.date
        if date_max is None or program.date > date_max:
            date_max = program.date
        channel_set.add(program.channel)

    stats_str = (
        f"**{len(channel_set)}** channels"
        f", **{num_programs:,}*** programs"
        f", **{all_play_time/60:,.1f}** hours playtime"
        f" between **{date_min.date()}** and **{date_max.date()}**\n"
    )
    stats_str += f"\n\n### playtime per genre (top {top_count})\n\n"

    sorted_genres = sorted(genre_counter, key=lambda k: genre_counter[k], reverse=True)
    values = [
        (
            f"{genre_counter[key] / 60:,.1f}h",
            f"{genre_counter[key] / all_play_time * 100:.2f}%",
            key,
        )
        for key in sorted_genres[:top_count]
    ]
    max_length_1 = max(len(v[0]) for v in values)
    max_length_2 = max(len(v[1]) for v in values)
    for v in values:
        stats_str += f"    {v[0]:{max_length_1}} {v[1]:{max_length_2}} {v[2]}\n"

    return f"## Statistics\n\n{stats_str}"


def write_stats(verbose: bool = False):
    readme = (PROJECT_PATH / "README.md").read_text()

    readme = readme[:readme.index("## Statistics")]

    readme += create_stats_str(verbose=verbose)

    (PROJECT_PATH / "README.md").write_text(readme)


if __name__ == "__main__":
    main(**parse_args())

