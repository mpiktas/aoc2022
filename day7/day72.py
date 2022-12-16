"""Advent of code 2022, day 7"""
from anytree import Node, Resolver, ResolverError
from day71 import get_dir_size


def day72():
    """Run the day 7 part 2"""
    with open("day7/input.txt", encoding="utf-8") as file:
        lines = [line.rstrip() for line in file]

    top = Node("top")
    curdir = top
    nodetrack = Resolver("name")
    for line in lines:
        if line[:4] == "$ cd":
            dirname = line[5:]
            if dirname == "..":
                curdir = nodetrack.get(curdir, "..")
            else:
                try:
                    curdir = nodetrack.get(curdir, dirname)
                except ResolverError:
                    curdir = Node(dirname, parent=curdir)
        if line[0] != "$":
            if line[:3] == "dir":
                Node(line[4:], parent=curdir)
            else:
                size, filename = line.split(" ")
                Node(filename, size=int(size), parent=curdir, file=filename)

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
