"""Advent of code 2022, day 5"""


def read_stack(stack_no, stacks):
    sl = [list(x) for x in stacks]
    i = 1 + stack_no * 4
    res = [x[i] for x in sl]
    return res


def day51():
    """Day 5, part 1"""

    with open("day5/input.txt", encoding="utf-8") as file:
        lines = [line.rstrip() for line in file]

    piles = []
    for i in range(9):
        piles.append(read_stack(i, lines[:8]))


if __name__ == "__main__":
    day51()
