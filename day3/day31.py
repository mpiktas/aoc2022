"""Advent of Code, day 3 """
import string

PRIORITIES = list(string.ascii_lowercase) + list(string.ascii_uppercase)


def calculate_priority(rucksack):
    """Calculate the priority for first task of day 3"""
    half = len(rucksack) // 2
    i = list(set(rucksack[:half]).intersection(rucksack[-half:]))
    if i:
        return PRIORITIES.index(i[0]) + 1

    print(str)
    print(i)
    return 0


def day31():
    """Do the task1 of day 3"""
    with open("day3/input.txt", encoding="utf-8") as file:
        lines = [line.rstrip() for line in file]

    tot = 0
    for dummy, value in enumerate(lines):
        tot = tot + calculate_priority(value)

    print(tot)

    priorities = [calculate_priority(x) for x in lines]

    print(sum(priorities))


if __name__ == "__main__":
    day31()
