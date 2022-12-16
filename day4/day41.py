"""Advent of code 2022, day 4"""


def compare1(pair1, pair2):
    """Compare two pairs"""
    return (pair1[0] <= pair2[0]) & (pair1[1] >= pair2[1])


def compare2(pairs1, pairs2):
    """Make comparison symmetrical"""
    return compare1(pairs1, pairs2) | compare1(pairs2, pairs1)


def str_to_int(string):
    """Convert string to integer"""
    return [int(x) for x in string]


def treat_line(line):
    """Read the pairs from the line and compare them"""
    line = [str_to_int(x.split("-")) for x in line.split(",")]
    return compare2(line[0], line[1])


def day41():
    """Day 4, task 1"""
    with open("day4/input.txt", encoding="utf-8") as file:
        lines = [line.rstrip() for line in file]

    pairs = [treat_line(x) for x in lines]

    print(sum(pairs))


if __name__ == "__main__":
    day41()
