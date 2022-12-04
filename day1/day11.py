"""Advent of code 2022, Day 1"""


def day11():
    """Day 1 task, first half"""

    with open("day1/input.txt", encoding="utf-8") as file:
        lines = [line.rstrip() for line in file]

    elf = 1
    calories = 0
    max_calories = 0
    for dummy, value in enumerate(lines):
        if value != "":
            calories = calories + int(value)
        else:
            elf = elf + 1
            if calories > max_calories:
                max_calories = calories
            calories = 0

    print(max_calories)


if __name__ == "__main__":
    day11()
