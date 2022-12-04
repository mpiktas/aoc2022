with open("day4/input.txt") as file:
    lines = [line.rstrip() for line in file]

def compare1(r1, r2): 
    return ((r1[0]<=r2[0]) & (r1[1]>=r2[1]))


def compare2(r1, r2):
    return (compare1(r1,r2) | compare1(r2, r1))


def str_to_int(s) :
    return [int(x) for x in s] 

def treat_line(s): 
    s = [str_to_int(x.split("-")) for x in s.split(",")]       
    return compare2(s[0], s[1])

cs = [treat_line(x) for x in lines]

print(sum(cs))