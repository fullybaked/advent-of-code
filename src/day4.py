import click


def load_data():
    file_data = open("data/day4.txt", "r").read()
    data = file_data.split("\n\n")

    line = data.pop(0)
    calls = [int(n) for n in line.rstrip("\n").split(",")]

    boards = []
    for board in data:
        boards.append(Board(board))

    return (calls, boards)


class Board:
    _rows: list[list[int]]
    _cols: list[list[int]]
    _row_len: int = 0
    _last_called: int | None = None
    _finished: bool = False

    def __init__(self, board_values: str):
        """
        Board values should be a string with each row on a new line
        and each number split by a space.
        """
        row_data = board_values.split("\n")
        rows = [[int(num) for num in row.split()] for row in row_data]
        self._rows = rows
        self._row_len = len(rows[0])
        self._cols = self._make_cols()

    def play(self, num: int):
        """
        Walk the board and compare the given number
        """
        self._last_called = num
        for r, row in enumerate(self._rows):
            for c, col in enumerate(row):
                if col == num:
                    if self.check_win(r, c):
                        return self.generate_score()

    def check_win(self, row, col) -> bool:
        """
        Remove the value of the called number
        and return whether the board has been won
        """
        matcher = [None] * self._row_len
        self._rows[row][col] = None
        if self._rows[row] == matcher:
            self._finished = True
            return True

        self._cols[col][row] = None
        if self._cols[col] == matcher:
            self._finished = True
            return True

        return False

    def finished(self) -> bool:
        return self._finished

    def _make_cols(self):
        flat_board = sum(self._rows, [])
        total_len = len(flat_board)
        cols = []
        for i in range(self._row_len):
            cols.append(flat_board[i : total_len : self._row_len])

        return cols

    def generate_score(self):
        score = 0
        for row in self._rows:
            for col in row:
                if col is not None:
                    score += col
        return score * self._last_called


class Game:
    def __init__(self, boards, calls):
        self._boards = boards
        self._calls = calls
        self._scores = []

    def play(self):
        for call in self._calls:
            for board in self._boards:
                if not board.finished():
                    score = board.play(call)
                    if score is not None:
                        self._scores.append(score)

    def winner(self):
        return self._scores[0]

    def looser(self):
        return self._scores[-1]


def main():
    calls, boards = load_data()
    game = Game(boards, calls)
    game.play()

    click.echo("Part 1")
    click.echo(f"Winner score: {game.winner()}")
    click.echo("Part 2")
    click.echo(f"Looser score {game.looser()}")
