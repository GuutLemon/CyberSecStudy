with open("day1.txt") as f:
    instr = f.read().strip()
    instr = [1 if i == '(' else -1 for i in instr]

# Part 1
def find_floor(instr):
    return sum(instr)

# Part 2
def find_pos(instr):
    floor = 0
    i = 0
    while floor > -1:
        floor += instr[i]
        i += 1
    return i

print(find_floor(instr))
print(find_pos(instr))