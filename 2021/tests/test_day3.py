import pytest
import src.day3 as day

EXAMPLE_IN = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]

COLUMNS = [
    "011110011100",
    "010001010101",
    "111111110000",
    "011101100011",
    "000111100100",
]


def test_bin_2_int():
    assert day.bin_2_int("01001") == 9


def test_diagnostics():
    assert day.diagnostics(EXAMPLE_IN) == 198


def test_atmosphere():
    assert day.atmosphere(EXAMPLE_IN) == 230


def test_common_bit():
    assert day.commonality(COLUMNS, 0, "0") == {"mc": "1", "lc": "0"}
    assert day.commonality(COLUMNS, 1, "1") == {"mc": "0", "lc": "1"}
    assert day.commonality(COLUMNS, 4, "0") == {"mc": "0", "lc": "1"}


def test_bit_columns():
    assert day.bit_columns(EXAMPLE_IN) == COLUMNS
