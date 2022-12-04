with open("day2/input.txt") as file:
    lines = [line.rstrip() for line in file]


points = {"A": 1, "B": 2, "C": 3}

win = {"AA": 3, "AB": 6, "AC": 0, "BA": 0, "BB": 3, "BC": 6, "CA": 6, "CB": 0, "CC": 3}

result = {
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

cr = {"X": "A", "Y": "B", "Z": "C"}

ending = {"X": 0, "Y": 3, "Z": 6}


def calculate_game_points(p1, p2, points=points, result=result, ending=ending):
    pkey = f"{p1}{p2}"
    return ending[p2] + points[result[pkey]]


tot = 0
for i, value in enumerate(lines):
    p = value.split()
    tot = tot + calculate_game_points(p[0], p[1])

print(tot)
