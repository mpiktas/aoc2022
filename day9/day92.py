"""Advent of code 2022, day 9"""

from day91 import HEAD_MOVES, add, read_moves, relative_tail, tail_to_str, test_rope

KNOT_MOVES = {
    "00_[0, 1]": [1, 1],
    "00_[1, 0]": [1, 1],
    "00_[-1, 1]": [0, 1],
    "00_[1, -1]": [1, 0],
    "00_[1, 1]": [1, 1],
    "01_[1, 0]": [1, 0],
    "01_[1, 1]": [1, 1],
    "01_[1, -1]": [1, -1],
    "02_[1, 1]": [1, 0],
    "02_[1, 0]": [1, -1],
    "02_[1, -1]": [1, -1],
    "02_[0, -1]": [1, -1],
    "02_[-1, -1]": [0, -1],
    "12_[1, -1]": [1, -1],
    "12_[0, -1]": [0, -1],
    "12_[-1, -1]": [-1, -1],
    "22_[1, -1]": [0, -1],
    "22_[0, -1]": [-1, -1],
    "22_[-1, -1]": [-1, -1],
    "22_[-1, 0]": [-1, -1],
    "22_[-1, 1]": [-1, 0],
    "21_[-1, -1]": [-1, -1],
    "21_[-1, 0]": [-1, 0],
    "21_[-1, 1]": [-1, 1],
    "20_[-1, -1]": [-1, 0],
    "20_[-1, 0]": [-1, 1],
    "20_[-1, 1]": [-1, 1],
    "20_[0, 1]": [-1, 1],
    "20_[1, 1]": [0, 1],
    "10_[-1, 1]": [-1, 1],
    "10_[0, 1]": [0, 1],
    "10_[1, 1]": [1, 1],
}


class RopeN:
    """Class for tracking rope movements"""

    def __init__(self, start, knot_count):
        self.knot_count = knot_count
        # do not use * for initializing the lists. Use [l for i in range(n)] instead.
        self.knots = [start] * knot_count
        self.knot_trace = [[start]] * knot_count
        self.tail_trace = [start]

    def move(self, step):
        """Move the rope by one"""

        moves = [None] * self.knot_count
        moves[0] = HEAD_MOVES[step]
        for i in range(self.knot_count - 1):
            hcoord = relative_tail(self.knots[i], self.knots[i + 1])
            key = "".join(hcoord) + "_" + str(moves[i])
            if (knot_move := KNOT_MOVES.get(key)) is None:
                knot_move = [0, 0]
            moves[i + 1] = knot_move

        for i in range(self.knot_count):
            self.knots[i] = add(self.knots[i], moves[i])
            self.knot_trace[i] = self.knot_trace[i] + [self.knots[i].copy()]
        self.tail_trace.append(self.knots[self.knot_count - 1])

        for i in range(self.knot_count - 1):
            tst = test_rope(self.knots[i], self.knots[i + 1])
            if not tst:
                print(str([x[-1] for x in self.knot_trace]))
                print(str(self.knots))
                print(str(moves))
                raise RuntimeError("Tail is too far away from the head")

    def move_multiple(self, command):
        """Move the rope head multiple times"""
        for dummy in range(int(command[1])):
            self.move(command[0])


def day92(filename):
    """Do task 2 of day 9"""

    moves = read_moves(filename)

    rope = RopeN([0, 0], 10)

    for single_move in moves:
        rope.move_multiple(single_move)

    tail_visits = {tail_to_str(x) for x in rope.tail_trace}

    print(str(tail_visits))
    print(len(tail_visits))


if __name__ == "__main__":
    day92("day9/input.txt")
