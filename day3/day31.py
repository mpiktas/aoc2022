"""Advent of Code, day 3 """
import string

PRIORITIES = list(string.ascii_lowercase) + list(string.ascii_uppercase)


def calculate_priority(s):
    n = len(s) // 2
    i = list(set(s[:n]).intersection(s[-n:]))
    if i:
        return PRIORITIES.index(i[0]) + 1
    else:
        print(s)
        print(i)
        return 0


def day31():

    with open("day3/input.txt") as file:
        lines = [line.rstrip() for line in file]

    tot = 0
    for i, value in enumerate(lines):
        tot = tot + calculate_priority(value)

    print(tot)

    pp = [calculate_priority(x) for x in lines]

    print(sum(pp))


if __name__ == "__main__":
    day31()
