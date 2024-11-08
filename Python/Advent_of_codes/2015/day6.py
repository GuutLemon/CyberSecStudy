from collections import defaultdict

with open('day6.txt') as f:
    instr = f.read().strip().replace('through ', '').replace('turn ', '').split('\n')
    instr = [i.split() for i in instr]
    instr = [[i[0], eval(f'({i[1]})'), eval(f'({i[2]})')] for i in instr]


grid = defaultdict(int)
def lights(part, instr, grid):
    for i in instr:
        x_start = min(i[1][0], i[2][0])
        x_range = (x_start, x_start + abs(i[1][0] - i[2][0]) + 1)
        y_start = min(i[1][1], i[2][1])
        y_range = (y_start ,y_start + abs(i[1][1] - i[2][1]) + 1)
        cmd = i[0]

        if part == 1:
            for x in range(*x_range):
                for y in range(*y_range):
                    if cmd == 'on':
                        grid[(x, y)] = True
                    elif cmd == 'off':
                        grid[(x, y)] = False
                    elif cmd == 'toggle':
                        grid[(x, y)] = not grid[(x, y)]

        elif part == 2:
            for x in range(*x_range):
                for y in range(*y_range):
                    if cmd == 'on':
                        grid[(x, y)] += 1
                    elif cmd == 'off' and grid[(x, y)] > 0:
                        grid[(x, y)] -= 1
                    elif cmd == 'toggle':
                        grid[(x, y)] += 2

    return sum(grid.values())


print(lights(1, instr, grid))
