import click

import src.day1


def load_data(day):
    return open(f"data/day{day}.txt").read().splitlines()


@click.command()
@click.option("--day", prompt="Enter which day you want to run")
def days(day):
    raw_data = load_data(day)
    if day == "1":
        src.day1.main(raw_data)


if __name__ == "__main__":
    days()
