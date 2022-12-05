import sys

from aocd import data

part = 1
if len(sys.argv) == 2:
    part = int(sys.argv[1])

my_score = 0

input = data.splitlines()

bonus = {"win": 6, "draw": 3, "loss": 0}
score = {"rock": 1, "paper": 2, "scissors": 3}
my_hand = {"X": "rock", "Y": "paper", "Z": "scissors"}

if part == 1:
    conditions = {
        "A X": "draw",
        "A Y": "win",
        "A Z": "loss",
        "B X": "loss",
        "B Y": "draw",
        "B Z": "win",
        "C X": "win",
        "C Y": "loss",
        "C Z": "draw",
    }

    for game in input:
        state = conditions[game]
        hand = my_hand[game.split()[1]]
        my_score += bonus[state] + score[hand]

    print(my_score)

if part == 2:
    opponent = {"A": "rock", "B": "paper", "C": "scissors"}
    my_play = {"X": "loss", "Y": "draw", "Z": "win"}
    win = {"A": "paper", "B": "scissors", "C": "rock"}
    loss = {"A": "scissors", "B": "rock", "C": "paper"}

    for game in input:
        them, me = game.split()

        if me == "X":
            # i should lose
            my_hand = loss[them]
        elif me == "Y":
            # i should draw
            my_hand = opponent[them]
        elif me == "Z":
            # i should win
            my_hand = win[them]

        state = my_play[me]
        my_score += score[my_hand] + bonus[state]

    print(my_score)
