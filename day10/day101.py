"""AOC 2022, day 10, part 1"""

# The task is off by one cycle. Even looking at the task and counting manually
# the test example does not produce the result in the task. You need to decrease
# the cycle count by one to get the correct result.


def read_instructions(filename):
    """Read the instructions"""
    with open(filename, encoding="utf-8") as file:
        lines = [line.rstrip() for line in file]
    return [x.split(" ") for x in lines]


def reg_history(instr):
    """Get the registry history"""
    regx = [1]
    cycle = 0
    for cmd in instr:
        if cmd[0] == "noop":
            regx.append(regx[cycle])
            cycle = cycle + 1
        if cmd[0] == "addx":
            regx.append(regx[cycle])
            regx.append(regx[cycle] + int(cmd[1]))
            cycle = cycle + 2
        if (cmd[0] != "noop") and (cmd[0] != "addx"):
            raise RuntimeError("Wrong input")
    return regx


def day101(filename):
    """Do part 1 of day 10 task"""
    instr = read_instructions(filename)

    regx = reg_history(instr)

    signals = [regx[i - 1] for i in [20, 60, 100, 140, 180, 220]]

    print(signals)
    signals = [regx[i - 1] * i for i in [20, 60, 100, 140, 180, 220]]
    print(sum(signals))


if __name__ == "__main__":
    day101("day10/input.txt")
