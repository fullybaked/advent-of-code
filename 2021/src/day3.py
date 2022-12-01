from collections import Counter

import click


def bit_columns(data):
    columns = [""] * len(data[0])
    for d in data:
        for i, c in enumerate(d):
            columns[i] = columns[i] + str(c)

    return columns


def commonality(columns, index, decider):
    # most_common returns list of tuples in the format (value, frequency)
    most, least = Counter(columns[index]).most_common()
    if most[1] == least[1]:
        most_common = decider
    else:
        most_common = most[0]

    if most_common == "1":
        return {"mc": "1", "lc": "0"}
    else:
        return {"mc": "0", "lc": "1"}


def bin_2_int(binary):
    return int(binary, 2)


def diagnostics(data):
    columns = bit_columns(data)

    gamma = ""
    epsilon = ""
    for i in range(len(data[0])):
        gamma += commonality(columns, i, "1")["mc"]
        epsilon += commonality(columns, i, "0")["lc"]

    return bin_2_int(gamma) * bin_2_int(epsilon)


def parse(data, index, mc_or_lc="mc"):
    _data = data.copy()
    columns = bit_columns(_data)
    common = commonality(columns, index, "1")[mc_or_lc]
    for value in data:
        if value[index] != common and value in _data and len(_data) > 1:
            _data.remove(value)
    return _data


def atmosphere(data):
    o2 = data.copy()
    co2 = data.copy()
    for i in range(len(data[0])):
        if len(o2) > 1:
            o2 = parse(o2, i, "mc")
        if len(co2) > 1:
            co2 = parse(co2, i, "lc")

    return bin_2_int(o2[0]) * bin_2_int(co2[0])


def main(raw_data):
    click.echo("Part 1")
    click.echo(f"Power consumption: {diagnostics(raw_data)}")
    click.echo("Part 2")
    click.echo(f"Life support: {atmosphere(raw_data)}")
