"""Advent of code 2022, day 6"""


def day62():
    """Solve the part 2 of day 6"""
    with open("day6/input.txt", encoding="utf-8") as file:
        lines = [line.rstrip() for line in file]
    inp = list(lines[0])
    for i in range(14, len(inp)):
        roll = set(inp[i - 14 : i])
        if len(roll) == 14:
            print(i)
            break


if __name__ == "__main__":
    day62()
