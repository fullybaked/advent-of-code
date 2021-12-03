import click


def create_windows(values: list[int]) -> list[int]:
    out = []
    for count, value in enumerate(values):
        if count + 2 < len(values):
            out.append(value + values[count + 1] + values[count + 2])

    return out


def count_increases(values: list[int]) -> int:
    out = 0
    for count, value in enumerate(values):
        if count == 0:
            continue
        prev = values[count - 1]
        if value > prev:
            out += 1

    return out


def main(raw_data):
    data = [int(d) for d in raw_data]
    count = count_increases(data)
    click.echo("Part 1")
    click.echo(f"There were [{count}] increases in depth")
    click.echo("Part 2")
    count = count_increases(create_windows(data))
    click.echo(f"There were [{count}] increases in depth")
