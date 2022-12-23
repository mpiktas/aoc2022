"""Advent of code 2022, day 7"""
from anytree import Node
from day71 import create_tree, get_dir_size


def day72():
    """Run the day 7 part 2"""
    with open("day7/input.txt", encoding="utf-8") as file:
        lines = [line.rstrip() for line in file]

    top = Node("top")

    create_tree(top, lines)
    dirsizes = {}
    get_dir_size(top.children[0], dirsizes)

    dirsizes1 = [value for (key, value) in dirsizes.items()]
    dirsizes1.sort()
    dirsizes2 = [70000000 - (dirsizes1[-1] - value) for value in dirsizes1]

    indexes = [index for index, value in enumerate(dirsizes2) if value > 30000000]
    indexes.sort()
    print(dirsizes1[indexes[0]])


if __name__ == "__main__":
    day72()
