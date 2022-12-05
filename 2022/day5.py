import os
import re
import sys
from collections import deque
from typing import List

from aocd import lines

example = []


class Stack:
    def __init__(self):
        self.stack = deque([])

    def add_to_bottom(self, crate):
        self.stack.appendleft(crate)

    def add_to_top(self, crate):
        self.stack.append(crate)

    def top_crate(self) -> str:
        return self.stack[len(self.stack) - 1]

    def remove_crate(self) -> str:
        return self.stack.pop()

    def __repr__(self) -> str:
        return "".join(self.stack)

    def remove_crates(self, number_of_crates) -> "Stack":
        stack = Stack()
        for _i in range(number_of_crates):
            stack.add_to_bottom(self.remove_crate())
        return stack

    def __iadd__(self, other: "Stack"):
        self.stack += other.stack
        return self


class Cargo:
    stacks = []

    def __init__(self, initial_state: List[str]):
        crates = initial_state[:-1]
        stacks = initial_state[-1]
        for i in range(1, 10):
            index = stacks.find(str(i))
            stack = Stack()
            for row in crates:
                if row[index] != " ":
                    stack.add_to_bottom(row[index])
            self.stacks.append(stack)

    def move_crates(self, move_command: str, bulk: bool = False):
        """
        Takes a move command in the string format

        move 4 from 6 to 9

        and moves the number of crates between the two stacks

        Accepts an option bulk flag, which defaults to False.
        If False it moves one crate at a time, which changes the order of the crates.
        If True, it moves the crates in temporary stack of size "count" maintaining
        their original order
        """
        moves = re.match(
            "^move (?P<count>\d+) from (?P<source>\d+) to (?P<dest>\d+$)", move_command
        )
        if bulk:
            # stacks are 0 indexed, but commands are not
            self.bulk_move(
                int(moves["count"]), int(moves["source"]) - 1, int(moves["dest"]) - 1
            )
        else:
            for i in range(int(moves["count"])):
                # stacks are 0 indexed, but commands are not
                self.move(int(moves["source"]) - 1, int(moves["dest"]) - 1)

    def move(self, source: int, dest: int):
        """
        Move the top crate from the source stack to the destination stack
        """
        crate = self.stacks[source].remove_crate()
        self.stacks[dest].add_to_top(crate)

    def bulk_move(self, count: int, source: int, dest: int):
        """
        Move the count of crates from source stack to destination stack maintaining
        the order they are in
        """
        stack = self.stacks[source].remove_crates(count)
        self.stacks[dest] += stack

    def top_row(self):
        row = ""
        for stack in self.stacks:
            row += stack.top_crate()
        return row


def get_crates_and_moves(lines: List[str]) -> tuple():
    space = lines.index("")
    # add 1 to the space to drop it from the slice
    split = slice(lines, space)
    crates = lines[: split.stop]
    moves = lines[split.stop + 1 :]
    return (crates, moves)


def part_1(lines: List[str]):
    crates, moves = get_crates_and_moves(lines)
    cargo = Cargo(crates)
    for move in moves:
        cargo.move_crates(move)

    print(cargo.top_row())


def part_2(lines: List[str]):
    crates, moves = get_crates_and_moves(lines)
    cargo = Cargo(crates)
    for move in moves:
        cargo.move_crates(move, True)

    print(cargo.top_row())


if __name__ == "__main__":
    part = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    debug = bool(os.environ.get("DEBUG", False))
    data = example if debug else lines

    locals()[f"part_{part}"](data)
