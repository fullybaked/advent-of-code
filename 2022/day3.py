import sys
from typing import List

from aocd import data

part = int(sys.argv[1]) if len(sys.argv) > 1 else 1


def priority(item):
    if item.isupper():
        return ord(item) - ord("A") + 27
    else:
        return ord(item) - ord("a") + 1


input = data.splitlines()
score = 0

if part == 1:
    for bag in input:
        split_at = len(bag) // 2
        compartment_1 = bag[:split_at]
        compartment_2 = bag[split_at:]

        common = set(compartment_1).intersection(set(compartment_2)).pop()

        score += priority(common)

    print(score)


if part == 2:

    score = 0

    def groups(bags: List[str]) -> List[List[str]]:
        groups = []
        for i in range(0, len(bags), 3):
            group = bags[i : i + 3]
            groups.append(group)
        return groups

    for group in groups(input):
        set1 = set(group[0])
        set2 = set(group[1])
        set3 = set(group[2])

        common = set1.intersection(set2, set3).pop()
        score += priority(common)

    print(score)
