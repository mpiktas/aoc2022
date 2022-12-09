"""Advent of code 2022, day 5"""


def read_stack(stack_no, stacks):
    """Read in the stacks at the beginning of the input"""
    stack_list = [list(x) for x in stacks]
    i = 1 + stack_no * 4
    res = [x[i] for x in stack_list]
    return res


def remove_reverse(pile):
    """Remove empty strings and reverse the pile"""
    pile = [x for x in pile if x != " "]
    pile.reverse()
    return pile


def read_instructions(line):
    """Parse the instructions in the line"""
    line_list = line.split(" ")
    instruction = [int(line_list[i]) for i in [1, 3, 5]]
    return instruction


def transform_pile(pile, move):
    """Transdorm the pile according to instructions"""
    stack = pile[move[1] - 1][-move[0] :]
    stack.reverse()
    pile[move[1] - 1] = pile[move[1] - 1][: -move[0]]
    pile[move[2] - 1] = pile[move[2] - 1] + stack


def day51():
    """Day 5, part 1"""

    with open("day5/input.txt", encoding="utf-8") as file:
        lines = [line.rstrip() for line in file]

    pile_input = lines[:8]
    instr_input = lines[10:]

    piles = [read_stack(i, pile_input) for i in range(9)]

    piles = [remove_reverse(pile) for pile in piles]

    piles1 = piles.copy()

    for dummy, instr in enumerate(instr_input):
        move = read_instructions(instr)
        transform_pile(piles1, move)

    last_stack = [x[-1:] for x in piles1]
    print(str(last_stack))


if __name__ == "__main__":
    day51()
