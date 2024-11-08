from sympy.physics.units import coulombs

with open('day3.txt') as f:
    instr = f.read().strip()


directions = {'^': (1, 0), 'v': (-1, 0), '>': (0, 1), '<': (0, -1)}

# Part 1
def santa_deli(instr):
    houses = set()
    pos = (0, 0)
    houses.add(pos)
    for i in instr:
        pos = tuple(map(sum, zip(pos, directions[i])))
        houses.add(pos)
    return len(houses)

# Part 2
def double_deli(instr):
    houses = set()
    pos1 = (0, 0)
    pos2 = (0, 0)
    houses.add(pos1)
    for i in instr[::2]:
        pos1 = tuple(map(sum, zip(pos1, directions[i])))
        houses.add(pos1)
    for i in instr[1::2]:
        pos2 = tuple(map(sum, zip(pos2, directions[i])))
        houses.add(pos2)
    return len(houses)


print(santa_deli(instr))
print(double_deli(instr))
