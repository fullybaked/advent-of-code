import click


def calculate_position(data: list[tuple[str, str]]) -> int:
    chart = {
        "distance": 0,
        "depth": 0,
    }
    for direction in data:
        d = direction[0]
        v = int(direction[1])

        if d == "forward":
            chart["distance"] += v
        elif d == "down":
            chart["depth"] += v
        elif d == "up":
            chart["depth"] -= v

    return chart["depth"] * chart["distance"]


def calc_with_aim(data: list[tuple[str, str]]) -> int:
    chart = {
        "aim": 0,
        "distance": 0,
        "depth": 0,
    }

    for direction in data:
        d = direction[0]
        v = int(direction[1])

        if d == "forward":
            chart["distance"] += v
            chart["depth"] += chart["aim"] * v
        elif d == "down":
            chart["aim"] += v
        elif d == "up":
            chart["aim"] -= v

    return chart["depth"] * chart["distance"]


def main(raw_data):
    data = [tuple(line.split()) for line in raw_data]
    click.echo("Part 1")
    click.echo(f"Current position: {calculate_position(data)}")
    click.echo("Part 2")
    click.echo(f"Current position using AIM: {calc_with_aim(data)}")
