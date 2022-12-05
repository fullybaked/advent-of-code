import os
import sys
from typing import List

from aocd import lines

example = [
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7",
    "6-6,4-6",
    "2-6,4-8",
]


def get_elf_assignment(assignments, elf):
    elf = elf - 1
    start = int(assignments.split(",")[elf].split("-")[0])
    end = int(assignments.split(",")[elf].split("-")[1])
    return {
        "start": start,
        "end": end,
        # range isn't inclusive we need to add 1 to the top end
        "range": range(start, end + 1),
    }


def in_range(range_to_check, range_to_contain) -> bool:
    head = range_to_check[0]
    tail = range_to_check[-1]
    if head in range_to_contain and tail in range_to_contain:
        return True
    else:
        return False


def part_1(lines: List[str]):
    pair_doing_all_work = 0
    for line in lines:
        elf1 = get_elf_assignment(line, elf=1)
        elf2 = get_elf_assignment(line, elf=2)
        if in_range(elf1["range"], elf2["range"]) or in_range(
            elf2["range"], elf1["range"]
        ):
            pair_doing_all_work += 1

    print(pair_doing_all_work)


def part_2(lines: List[str]):
    overlaps = 0
    for line in lines:
        elf1 = get_elf_assignment(line, elf=1)
        elf2 = get_elf_assignment(line, elf=2)
        overlap = set(elf1["range"]).intersection(set(elf2["range"])) or set(
            elf2["range"]
        ).intersection(set(elf1["range"]))
        if len(overlap) > 0:
            overlaps += 1

    print(overlaps)


if __name__ == "__main__":
    part = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    debug = bool(os.environ.get("DEBUG", False))
    data = example if debug else lines

    locals()[f"part_{part}"](data)
