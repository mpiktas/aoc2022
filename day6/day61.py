"""Advent of code 2022, day 6"""


def day61():
    """Solve the part 1 of day 6"""
    with open("day6/input.txt", encoding="utf-8") as file:
        lines = [line.rstrip() for line in file]
    input = list(lines[0])
    for i in range(4, len(input)):
        roll = set(input[i - 4 : i])
        if len(roll) == 4:
            print(i)
            break


if __name__ == "__main__":
    day61()
