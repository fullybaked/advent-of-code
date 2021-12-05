from src.day4 import Board, Game, load_data
from unittest.mock import patch, mock_open

EXAMPLE_IN = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""


def test_play_boards_for_first_win():
    with patch("builtins.open", mock_open(read_data=EXAMPLE_IN)):
        calls, boards = load_data()
        game = Game(boards, calls)
        game.play()

        assert game.winner() == 4512


def test_play_boards_for_last_win():
    with patch("builtins.open", mock_open(read_data=EXAMPLE_IN)):
        calls, boards = load_data()
        game = Game(boards, calls)
        game.play()

        assert game.looser() == 1924


def test_record_win_row():
    board_data = """22 13 17 11 0
    8 2 23 4 24
    21 9 14 16 7
    6 10 3 18 5
    1 12 20 15 19
    """

    board = Board(board_data)

    assert board.check_win(0, 0) is False
    assert board.check_win(0, 1) is False
    assert board.check_win(0, 2) is False
    assert board.check_win(0, 3) is False
    assert board.check_win(0, 4) is True


def test_record_win_col():
    board_data = """22 13 17 11 0
    8 2 23 4 24
    21 9 14 16 7
    6 10 3 18 5
    1 12 20 15 19
    """

    board = Board(board_data)

    assert board.check_win(0, 0) is False
    assert board.check_win(1, 0) is False
    assert board.check_win(2, 0) is False
    assert board.check_win(3, 0) is False
    assert board.check_win(4, 0) is True


def test_cols():
    board_data = """22 13 17 11 0
    8 2 23 4 24
    21 9 14 16 7
    6 10 3 18 5
    1 12 20 15 19
    """

    cols = [
        [22, 8, 21, 6, 1],
        [13, 2, 9, 10, 12],
        [17, 23, 14, 3, 20],
        [11, 4, 16, 18, 15],
        [0, 24, 7, 5, 19],
    ]

    board = Board(board_data)

    assert board._cols == cols
