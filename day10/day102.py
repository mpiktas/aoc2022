"""AOC 2022, day 10, part 2"""

from day101 import read_instructions, reg_history


def day102(filename):
    """Do part 2 of day 10 task"""
    instr = read_instructions(filename)

    regx = reg_history(instr)
    draw = []
    for cycle in range(1, len(regx)):
        sprite = regx[cycle - 1]
        pos = cycle % 40 - 1
        if pos < 0:
            pos = 39
        print([cycle, pos, sprite])
        visible = [pos == x for x in [sprite - 1, sprite, sprite + 1]]
        print(visible)
        if sum(visible) > 0:
            draw.append("#")
        else:
            draw.append(".")

    crt = [
        "".join(draw[x[0] : x[1]])
        for x in [[0, 40], [40, 80], [80, 120], [120, 160], [160, 200], [200, 240]]
    ]
    for line in crt:
        print(line)


if __name__ == "__main__":
    day102("day10/input.txt")
