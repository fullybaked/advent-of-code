from collections import Counter

from aocd import data

elf = 1
elves = {f"elf-{elf}": 0}

for snack in data.splitlines():
    if snack == "":
        # move to next elf and initialise
        elf += 1
        elves[f"elf-{elf}"] = 0
    else:
        elves[f"elf-{elf}"] += int(snack)

count = Counter(elves)
has_most_food, calories = count.most_common(1)[0]

print(f"{has_most_food} has the most calories with {calories}")

top_three = count.most_common(3)
top_three_calories = []
for _, calories in top_three:
    top_three_calories.append(int(calories))

print(f"The top three elves have {sum(top_three_calories)} calories")
