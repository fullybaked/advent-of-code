from collections import namedtuple

import click

Point = namedtuple("Point", ["x", "y"])


def parse_data(data):
    segments = []
    for line in data:
        points = line.split(" -> ")
        start_x, start_y = points[0].split(",")
        end_x, end_y = points[1].split(",")
        segment = (
            Point(int(start_x), int(start_y)),
            Point(int(end_x), int(end_y)),
        )
        segments.append(segment)
    return segments


def map_size(segments):
    max_x = 0
    max_y = 0

    for start, end in segments:
        max_x = max(max_x, start.x, end.x)
        max_y = max(max_y, start.y, end.y)

    return (max_x, max_y)


def create_base_map(size):
    mapping = []
    for _ in range(size[1] + 1):
        _row = []
        for _ in range(size[0] + 1):
            _row.append(0)

        mapping.append(_row)

    return mapping


def plot(segments, mapping, include_diagonals=False):
    for start, end in segments:
        min_x = min(start.x, end.x)
        min_y = min(start.y, end.y)
        max_x = max(start.x, end.x)
        max_y = max(start.y, end.y)

        if min_x == max_x and min_y == max_y:
            mapping[min_y][min_x] += 1
        elif min_x == max_x:
            for y in range(min_y, max_y + 1):
                mapping[y][min_x] += 1
        elif min_y == max_y:
            for x in range(min_x, max_x + 1):
                mapping[min_y][x] += 1
        elif include_diagonals:
            for point in diagonals(start, end):
                mapping[point.y][point.x] += 1

    return mapping


def diagonals(start, end):
    if start.x < end.x:
        x = range(start.x, end.x + 1)
    else:
        x = range(start.x, end.x - 1, -1)

    if start.y < end.y:
        y = range(start.y, end.y + 1)
    else:
        y = range(start.y, end.y - 1, -1)

    x_vals = [i for i in x]
    y_vals = [i for i in y]

    diagonals = []
    for i, v in enumerate(x_vals):
        point = Point(v, y_vals[i])
        diagonals.append(point)

    return diagonals


def count_vents(plot):
    count = 0
    for row in plot:
        for col in row:
            if col >= 2:
                count += 1

    return count


def print_map(mapping):
    for row in mapping:
        line = "".join([str(i) for i in row]).replace("0", ".")
        print(line)


def main(raw_data):
    data = parse_data(raw_data)
    size = map_size(data)
    vents = create_base_map(size)
    vents = plot(data, vents)
    score = count_vents(vents)

    click.echo("Part 1")
    click.echo(f"There are [{score}] overlapping lines.")

    vents = create_base_map(size)
    vents_with_diags = plot(data, vents, include_diagonals=True)
    score = count_vents(vents_with_diags)
    click.echo("Part 2")
    click.echo(f"There are [{score}] overlapping lines including diagonals.")
