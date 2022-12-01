from unittest.mock import patch

from src.day1 import count_increases, create_windows

EXAMPLE_IN = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]


def test_part_1_single_increases():
    assert count_increases(EXAMPLE_IN) == 7


def test_create_windows():
    expected = [
        607,
        618,
        618,
        617,
        647,
        716,
        769,
        792,
    ]

    assert create_windows(EXAMPLE_IN) == expected


def test_part_2_window_increases():
    values = create_windows(EXAMPLE_IN)
    assert count_increases(values) == 5
