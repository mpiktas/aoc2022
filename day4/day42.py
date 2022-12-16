"""Advent of code 2022, task2"""

from day41 import str_to_int


def compare21(pair1, pair2):
    """Compare two pairs"""
    return (pair1[0] <= pair2[1]) & (pair1[1] >= pair2[0])


def compare22(pairs1, pairs2):
    """Do symmetrical comparison"""
    return compare21(pairs1, pairs2) | compare21(pairs2, pairs1)


def treat_line2(line):
    """Get the pairs from the line and compare them"""
    line = [str_to_int(x.split("-")) for x in line.split(",")]
    return compare22(line[0], line[1])


def day42():
    """Do task 2 of day 4"""

    with open("day4/input.txt", encoding="utf-8") as file:
        lines = [line.rstrip() for line in file]

    pairs = [treat_line2(x) for x in lines]

    print(sum(pairs))


if __name__ == "__main__":
    day42()
