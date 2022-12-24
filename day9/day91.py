"""Advent of code 2022, day 9"""


def read_moves(filename):
    """Read the moves"""
    with open(filename, encoding="utf-8") as file:
        lines = [line.rstrip() for line in file]
    return [x.split(" ") for x in lines]


TAIL_MOVES = {
    "00U": [1, 1],
    "00R": [1, 1],
    "01R": [1, 0],
    "02R": [1, -1],
    "02D": [1, -1],
    "12D": [-1, 0],
    "22L": [-1, -1],
    "22D": [-1, -1],
    "21L": [-1, 0],
    "20L": [-1, 1],
    "20U": [-1, 1],
    "10U": [0, 1],
}

HEAD_MOVES = {"U": [0, 1], "R": [1, 0], "D": [0, -1], "L": [-1, 0]}


def add(pos, move):
    print(pos)
    print(move)
    pos[0] = pos[0] + move[0]
    pos[1] = pos[1] + move[1]


def relative_tail(head, tail):
    res = [0, 0]
    res[0] = head[0] - tail[0] + 1
    res[1] = head[1] - tail[1] + 1
    return [str(x) for x in res]


class Rope:
    def __init__(self, start):
        self.head = start
        self.tail = start
        self.head_trace = [start]
        self.tail_trace = [start]

    def move(self, step):
        hcoord = relative_tail(self.head, self.tail)
        key = "".join(hcoord) + step
        if tail_move := TAIL_MOVES.get(key) is None:
            tail_move = [0, 0]
        self.tail = add(self.tail, tail_move)
        self.head = add(self.head, HEAD_MOVES[step])
        self.head_trace = self.head_trace.append(self.head)
        self.tail_trace = self.tail_trace.append(self.tail)

    def move_multiple(self, command):
        print(command)
        for x in range(int(command[1])):
            print(self.head)
            print(self.tail)
            self.move(command[0])


def day91(filename):
    """Do task 1 of day 9"""

    moves = read_moves(filename)

    rope = Rope([0, 0])
    rope.move_multiple(moves[0])

    [rope.move_multiple(x) for x in moves]
    print(len(set(rope.tail_trace)))


if __name__ == "__main__":
    day91("day9/input.txt")
