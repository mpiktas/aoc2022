import string

priorities = list(string.ascii_lowercase)+list(string.ascii_uppercase)

def calculate_priority(s, priorities = priorities):
    n = len(s)//2
    i = list(set(s[:n]).intersection(s[-n:]))
    if i:
        return priorities.index(i[0])+1
    else:
        print(s)
        print(i)
        return 0


with open("day3/input.txt") as file:
    lines = [line.rstrip() for line in file]

tot = 0
for i, value in enumerate(lines):
    tot = tot + calculate_priority(value)

print(tot)

pp = [calculate_priority(x) for x in lines]

print(sum(pp))

