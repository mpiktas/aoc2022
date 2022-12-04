with open("day2/input.txt") as file:
    lines = [line.rstrip() for line in file]


def calculate_game_points(p1, p2, cr, points, win):
    m = cr[p2]
    pkey = f'{p1}{m}'
    return win[pkey]+points[m]



points = {"A": 1, "B":2, "C" :3}
win = {"AA": 3, "AB": 6, "AC": 0, "BA": 0, "BB": 3, "BC": 6, "CA": 6, "CB": 0, "CC": 3}

cr = {"X": "A", "Y": "B", "Z":"C"}


tot = 0
for i, value in enumerate(lines):
    p = value.split()
    tot = tot + calculate_game_points(p[0], p[1], cr, points, win)

print(tot)




