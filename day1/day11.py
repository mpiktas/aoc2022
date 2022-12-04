with open("task1/input.txt") as file:
    lines = [line.rstrip() for line in file]

elf = 1
calories = 0
max_calories = 0 
for i, value in enumerate(lines):
    if value != '':
        calories = calories + int(value)
    else:
        elf = elf + 1
        if calories > max_calories:
            max_calories = calories
        calories = 0
        
print(max_calories)
        




