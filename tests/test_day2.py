from src.day2 import calc_with_aim, calculate_position

EXAMPLE_INPUT = [
    ("forward", "5"),
    ("down", "5"),
    ("forward", "8"),
    ("up", "3"),
    ("down", "8"),
    ("forward", "2"),
]


def test_calculate_position():
    assert calculate_position(EXAMPLE_INPUT) == 150


def test_calculate_with_aim():
    assert calc_with_aim(EXAMPLE_INPUT) == 900
