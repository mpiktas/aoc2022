"""Advent of code 2022, Day 1"""


def day12():
    """Day 1, part 2"""
    with open("day1/input.txt", encoding="utf-8") as file:
        lines = [line.rstrip() for line in file]

    calories = 0
    elf = []
    for dummy, value in enumerate(lines):
        if value != "":
            calories = calories + int(value)
        else:
            elf = elf + [calories]
            calories = 0

    elf.sort()
    print(sum(elf[-3:]))


if __name__ == "__main__":
    day12()
