"""Advent of code 2022, day 8"""

import numpy as np


def str_to_int_list(str):
    """Convert string to int list"""
    return [int(x) for x in list(str)]


def get_treemap(filename):
    """Read the treemap and return an array containing it"""
    with open(filename, encoding="utf-8") as file:
        lines = [line.rstrip() for line in file]

    return np.asarray([str_to_int_list(x) for x in lines])


def check_visibility(i, j, tmap):
    """Check tree visibility for a given cell"""
    # Check left
    left = sum(tmap[i, :j] >= tmap[i, j])
    right = sum(tmap[i, (j + 1) :] >= tmap[i, j])
    up = sum(tmap[:i, j] >= tmap[i, j])
    down = sum(tmap[(i + 1) :, j] >= tmap[i, j])
    return (left == 0) or (right == 0) or (up == 0) or (down == 0)


def day81(filename):
    """Do task 1 of day 8"""
    treemap = get_treemap(filename)
    visible = 0
    for i in range(1, treemap.shape[0] - 1):
        for j in range(1, treemap.shape[1] - 1):
            visible = visible + check_visibility(i, j, treemap)
    print(visible)
    print(visible + 2 * treemap.shape[0] + 2 * (treemap.shape[1] - 2))


if __name__ == "__main__":
    day81("day8/input.txt")
