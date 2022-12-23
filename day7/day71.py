"""Advent of code 2022, day 7"""
from anytree import Node, Resolver, ResolverError


def get_dir_size(root, hash_table):
    """Calculate the size of directory"""
    if len(root.children) == 0:
        return root.size

    for node in root.children:
        count = hash_table.get(str(root), 0)
        hash_table[str(root)] = count + get_dir_size(node, hash_table)
    return hash_table[str(root)]


def create_tree(top, lines):
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


def day71():
    """Run the day 7 part 1"""
    with open("day7/input.txt", encoding="utf-8") as file:
        lines = [line.rstrip() for line in file]

    top = Node("top")
    create_tree(top, lines)
    dirsizes = {}
    get_dir_size(top.children[0], dirsizes)

    filtered = [value for (key, value) in dirsizes.items() if value <= 100000]
    print(sum(filtered))


if __name__ == "__main__":
    day71()
