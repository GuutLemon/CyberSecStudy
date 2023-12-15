from collections import defaultdict

with open('day14.txt') as f:
    read_data = f.read().strip().split('\n')

grid = tuple([i for i in j] for j in read_data)


def tilting(grid, d) -> tuple:
    if d in 'we':
        lines = range(len(grid))
        values = range(len(grid[0]))
        if d == 'e':
            values = range(len(grid[0]) - 1, -1, -1)

        for i in lines:
            current_solid = (i, -1 if d == 'w' else len(grid[0]))
            for j in values:
                if grid[i][j] == '#':
                    current_solid = (i, j)
                elif grid[i][j] == 'O':
                    grid[i][j] = '.'
                    di, dj = (current_solid[0], current_solid[1] + 1*(d == 'w') - 1*(d == 'e'))
                    grid[di][dj] = 'O'
                    current_solid = (di, dj)

    elif d in 'ns':
        lines = range(len(grid[0]))
        values = range(len(grid))
        if d == 's':
            values = range(len(grid) - 1, -1, -1)

        for j in lines:
            current_solid = (-1 if d == 'n' else len(grid), j)
            for i in values:
                if grid[i][j] == '#':
                    current_solid = (i, j)
                elif grid[i][j] == 'O':
                    grid[i][j] = '.'
                    di, dj = (current_solid[0] + 1*(d == 'n') - 1*(d == 's'), current_solid[1])
                    grid[di][dj] = 'O'
                    current_solid = (di, dj)
    return grid


def cal_load(grid):
    weight = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                weight += len(grid) - i
    return weight

# Part 1
grid_1 = [i[::] for i in grid]
grid_1 = tilting(grid_1, 'n')
print('Part 1:', cal_load(grid_1))
# print(*grid, sep='\n')

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
print('Part 2:', cal_load(grid))
