with open("day1/input.txt") as file:
    lines = [line.rstrip() for line in file]


calories = 0
elf = []
for i, value in enumerate(lines):
    if value != "":
        calories = calories + int(value)
    else:
        elf = elf + [calories]
        calories = 0


elf.sort()
print(sum(elf[-3:]))
