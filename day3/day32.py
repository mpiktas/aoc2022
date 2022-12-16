"""Advent of code, day 3, task 2"""

import string

PRIORITIES = list(string.ascii_lowercase) + list(string.ascii_uppercase)


def calculate_priority2(rucksack):
    """Calculate the priority for the task 2"""
    i = set(rucksack[0]).intersection(rucksack[1]).intersection(rucksack[2])
    return PRIORITIES.index(list(i)[0]) + 1


def day32():
    """Do task 2 of day 3"""

    with open("day3/input.txt", encoding="utf-8") as file:
        lines = [line.rstrip() for line in file]

    tot = 0
    for i in range(3, len(lines) + 3, 3):
        tot = tot + calculate_priority2(lines[i - 3 : i])

    print(tot)


if __name__ == "__main__":
    day32()
