from collections import defaultdict

with open('day14.txt') as f:
    read_data = f.read().strip().split('\n')

grid = tuple([i for i in j] for j in read_data)


def tilting(grid, d) -> tuple:
    if d in 'we':
        lines = range(len(grid))
        values = range(len(grid[0]))
        if d == 'e':
            grid = tuple(i[::-1] for i in grid)

        for i in lines:
            current_solid = (i, -1)
            for j in values:
                if grid[i][j] == '#':
                    current_solid = (i, j)
                elif grid[i][j] == 'O':
                    grid[i][j] = '.'
                    di, dj = (current_solid[0], current_solid[1] + 1)
                    grid[di][dj] = 'O'
                    current_solid = (di, dj)

    elif d in 'ns':
        lines = range(len(grid[0]))
        values = range(len(grid))
        if d == 's':
            grid = grid[::-1]

        for j in lines:
            current_solid = (-1, j)
            for i in values:
                if grid[i][j] == '#':
                    current_solid = (i, j)
                elif grid[i][j] == 'O':
                    grid[i][j] = '.'
                    di, dj = (current_solid[0] + 1, current_solid[1])
                    grid[di][dj] = 'O'
                    current_solid = (di, dj)

    if d == 'e':
        grid = tuple(i[::-1] for i in grid)
    elif d == 's':
        grid = grid[::-1]
    return grid


def cal_load(grid):
    weight = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                weight += len(grid) - i
    return weight

# Part 1
# grid_1 = tilting(grid, 'n')
# print(cal_load(grid_1))

def mega_tilt(grid):
    for d in 'nwse':
        grid = tilting(grid, d)
    return grid

def omega_tilt(grid):
    end = 1000000000
    i = 1   # Start time at 1
    cycling = False
    seen = {}
    while i <= end:
        grid = mega_tilt(grid)
        i += 1
        s = str(grid)   # stop_dictionary_complaining_about_unhashable
        if not cycling and s in seen:
            repeat_period = i - seen[s]     # seen[s]: How many step between first repeating a result
            i = end - ((end - seen[s]) % repeat_period)   # Bring i to the start of the last cycle
            cycling = True
        seen[s] = i
    return grid

grid = omega_tilt(grid)
print(cal_load(grid))
