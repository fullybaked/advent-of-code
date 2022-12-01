from src.day5 import (
    Point,
    count_vents,
    create_base_map,
    diagonals,
    map_size,
    parse_data,
    plot,
)

EXAMPLE_IN = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""

EXAMPLE_OUT = [
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 2, 1, 1, 1, 2, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 1, 1, 1, 0, 0, 0, 0],
]

EXAMPLE_WITH_DIAGS = [
    [1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 2, 0, 0],
    [0, 0, 2, 0, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 2, 0, 2, 0, 0],
    [0, 1, 1, 2, 3, 1, 3, 2, 1, 1],
    [0, 0, 0, 1, 0, 2, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [2, 2, 2, 1, 1, 1, 0, 0, 0, 0],
]


def test_map_size():
    data = parse_data(EXAMPLE_IN.splitlines())
    size = map_size(data)

    assert size == (9, 9)


def test_starter_map():
    data = parse_data(EXAMPLE_IN.splitlines())
    size = map_size(data)

    empty_map = create_base_map(size)

    assert empty_map == [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]


def test_plotter():
    data = parse_data(EXAMPLE_IN.splitlines())
    size = map_size(data)
    empty_map = create_base_map(size)

    vents_map = plot(data, empty_map)

    assert vents_map == EXAMPLE_OUT


def test_count_vents():
    data = parse_data(EXAMPLE_IN.splitlines())
    size = map_size(data)
    empty_map = create_base_map(size)
    vents_map = plot(data, empty_map)

    assert count_vents(vents_map) == 5


def test_diagonals():
    start = Point(5, 5)
    end = Point(8, 2)

    expected = [
        Point(5, 5),
        Point(6, 4),
        Point(7, 3),
        Point(8, 2),
    ]

    assert diagonals(start, end) == expected


def test_plot_diagonals():
    data = parse_data(EXAMPLE_IN.splitlines())
    size = map_size(data)
    empty_map = create_base_map(size)
    vents_map = plot(data, empty_map, include_diagonals=True)

    assert vents_map == EXAMPLE_WITH_DIAGS


def test_score_with_diagonals():
    data = parse_data(EXAMPLE_IN.splitlines())
    size = map_size(data)
    empty_map = create_base_map(size)
    vents_map = plot(data, empty_map, include_diagonals=True)

    assert count_vents(vents_map) == 12
