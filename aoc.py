import click
from os.path import exists

import src.day1
import src.day2
import src.day3
import src.day4


def load_data(day):
    data_file = f"data/day{day}.txt"
    if exists(data_file):
        return open(data_file).read().splitlines()


@click.command()
@click.option("--day", prompt="Enter which day you want to run")
def days(day):
    raw_data = load_data(day)
    if day == "1":
        src.day1.main(raw_data)
    elif day == "2":
        src.day2.main(raw_data)
    elif day == "3":
        src.day3.main(raw_data)
    elif day == "4":
        src.day4.main()


if __name__ == "__main__":
    days()
