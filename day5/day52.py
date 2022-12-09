"""Advent of code 2022, day 5"""

from day51 import read_instructions, read_stack, remove_reverse


def transform_pile2(pile, move):
    """Transform the pile according to part 2 rules"""
    stack = pile[move[1] - 1][-move[0] :]
    remainder = pile[move[1] - 1][: -move[0]]
    pile[move[1] - 1] = remainder.copy()
    pile[move[2] - 1] = pile[move[2] - 1].copy() + stack


def day52():
    """Day 5, part 2"""

    with open("day5/input.txt", encoding="utf-8") as file:
        lines = [line.rstrip() for line in file]

    pile_input = lines[:8]
    instr_input = lines[10:]

    piles = [read_stack(i, pile_input) for i in range(9)]

    piles = [remove_reverse(pile) for pile in piles]

    piles1 = piles.copy()

    for dummy, instr in enumerate(instr_input):
        move = read_instructions(instr)
        transform_pile2(piles1, move)

    last_stack = [x[-1:] for x in piles1]
    print(str(last_stack))


if __name__ == "__main__":
    day52()
