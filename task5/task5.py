import string

priorities = list(string.ascii_lowercase)+list(string.ascii_uppercase)

def calculate_priority(s, priorities = priorities):
    i = set(s[0]).intersection(s[1]).intersection(s[2])
    return priorities.index(list(i)[0])+1
    

with open("task4/input.txt") as file:
    lines = [line.rstrip() for line in file]

tot = 0
for i in range(3, len(lines) + 3, 3):
   # print(i)
   # print(lines[i-3:i])
    tot = tot + calculate_priority(lines[i-3:i])

print(tot)

## s = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg"]
## s = ["wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]
## 
