"""Advent of code 2022, day 8"""

import numpy as np
from day81 import get_treemap


def first_true(arr):
    """Find first true. Return number of false found plus one if true found"""
    pos = 0
    for dummy, value in enumerate(arr):
        if not value:
            pos = pos + 1
        else:
            break
    if pos != arr.shape[0]:
        pos = pos + 1
    return pos


def scenic_score(i, j, tmap):
    """Check tree visibility for a given cell"""
    left = first_true(np.flip(tmap[i, :j] - tmap[i, j]) >= 0)
    right = first_true((tmap[i, (j + 1) :] - tmap[i, j]) >= 0)
    upd = first_true(np.flip(tmap[:i, j] - tmap[i, j]) >= 0)
    down = first_true((tmap[(i + 1) :, j] - tmap[i, j]) >= 0)
    return left * right * upd * down


def day82(filename):
    """Do task 2 of day 8"""
    treemap = get_treemap(filename)
    scores = np.zeros((treemap.shape[0] - 2, treemap.shape[1] - 2), dtype=int)
    for i in range(1, treemap.shape[0] - 1):
        for j in range(1, treemap.shape[1] - 1):
            scores[i - 1, j - 1] = scenic_score(i, j, treemap)
    print(np.max(scores))


if __name__ == "__main__":
    day82("day8/input.txt")
