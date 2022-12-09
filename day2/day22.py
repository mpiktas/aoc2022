"""Advent of code 2022, day 2"""


POINTS = {"A": 1, "B": 2, "C": 3}

WIN = {"AA": 3, "AB": 6, "AC": 0, "BA": 0, "BB": 3, "BC": 6, "CA": 6, "CB": 0, "CC": 3}

RESULT = {
    "AX": "C",
    "AY": "A",
    "AZ": "B",
    "BX": "A",
    "BY": "B",
    "BZ": "C",
    "CX": "B",
    "CY": "C",
    "CZ": "A",
}

MATCH_TABLE = {"X": "A", "Y": "B", "Z": "C"}

ENDING = {"X": 0, "Y": 3, "Z": 6}


def calculate_game_points2(player1, player2):
    """Calculate the game points for task 2"""
    pkey = f"{player1}{player2}"
    return ENDING[player2] + POINTS[RESULT[pkey]]


def day22():
    """Do day 2 part 2 task"""

    with open("day2/input.txt", encoding="utf-8") as file:
        lines = [line.rstrip() for line in file]

    total = 0
    for dummy, value in enumerate(lines):
        game = value.split()
        total = total + calculate_game_points2(game[0], game[1])

    print(total)


if __name__ == "__main__":
    day22()
