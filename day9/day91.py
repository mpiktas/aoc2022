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
    "12D": [0, -1],
    "22L": [-1, -1],
    "22D": [-1, -1],
    "21L": [-1, 0],
    "20L": [-1, 1],
    "20U": [-1, 1],
    "10U": [0, 1],
}

HEAD_MOVES = {"U": [0, 1], "R": [1, 0], "D": [0, -1], "L": [-1, 0]}


def add(pos, move):
    """Return the sum of two lists"""
    res = [0, 0]
    res[0] = pos[0] + move[0]
    res[1] = pos[1] + move[1]
    return res


def relative_tail(head, tail):
    """Calculate relative tail coordinates"""
    res = [0, 0]
    res[0] = -head[0] + tail[0] + 1
    res[1] = -head[1] + tail[1] + 1
    return [str(x) for x in res]


def test_rope(head, tail):
    """Test whether the rope tail and head at the correct distance"""
    c1 = abs(head[0] - tail[0])
    c2 = abs(head[1] - tail[1])
    return (c1 <= 1) & (c2 <= 1)


class Rope:
    def __init__(self, start):
        self.head = start
        self.tail = start
        self.head_trace = [start]
        self.tail_trace = [start]

    def move(self, step):
        """Move the rope head"""
        hcoord = relative_tail(self.head, self.tail)
        key = "".join(hcoord) + step

        if (tail_move := TAIL_MOVES.get(key)) is None:
            tail_move = [0, 0]

        self.tail = add(self.tail, tail_move)
        self.head = add(self.head, HEAD_MOVES[step])

        tst = test_rope(self.head, self.tail)
        if not tst:
            print(key)
            print(tail_move)
            print("Head at ")
            print(self.head)
            print("Tail at ")
            print(self.tail)
            raise RuntimeError("Tail is too far away from the head")

        self.head_trace.append(self.head)
        self.tail_trace.append(self.tail)

    def move_multiple(self, command):
        """Move the rope head multiple times"""
        for x in range(int(command[1])):
            self.move(command[0])


def tail_to_str(coord):
    """Convert list to string for comparison"""
    return ",".join([str(x) for x in coord])


def day91(filename):
    """Do task 1 of day 9"""

    moves = read_moves(filename)

    rope = Rope([0, 0])

    [rope.move_multiple(x) for x in moves]

    print(len(set([tail_to_str(x) for x in rope.tail_trace])))


if __name__ == "__main__":
    day91("day9/input.txt")
