"""Advent of code 2022, day 2"""

POINTS = {"A": 1, "B": 2, "C": 3}
WIN = {"AA": 3, "AB": 6, "AC": 0, "BA": 0, "BB": 3, "BC": 6, "CA": 6, "CB": 0, "CC": 3}
MATCH_TABLE = {"X": "A", "Y": "B", "Z": "C"}


def calculate_game_points(player1, player2, match_table, points, win):
    """Calculate the elf game points for the day 2, first part"""
    matched2 = match_table[player2]
    pkey = f"{player1}{matched2}"
    return win[pkey] + points[matched2]


def day21():
    """Day 2, part 1"""

    with open("day2/input.txt", encoding="utf-8") as file:
        lines = [line.rstrip() for line in file]

    tot = 0
    for dummy, value in enumerate(lines):
        party = value.split()
        tot = tot + calculate_game_points(party[0], party[1], MATCH_TABLE, POINTS, WIN)

    print(tot)


if __name__ == "__main__":
    day21()
