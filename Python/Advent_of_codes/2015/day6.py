from collections import defaultdict

def coords_format(lst: list):
    new_lst = []
    new_lst.append(lst[0])
    new_lst.append([int(i) for i in lst[1].split(",")])
    new_lst.append([int(i) for i in lst[2].split(",")])
    return new_lst


def light_config(action: str, start: list, stop: list, grid, part):
    x_range = None
    y_range = None
    # Get the arguments for range(), prepare for when start coords > stop coords
    if start[0] > stop[0]:
        x_range = [start[0], stop[0] - 1, -1]
    elif start[0] <= stop[0]:
        x_range = [start[0], stop[0] + 1]
    if start[1] > stop[1]:
        y_range = [start[1], stop[1] - 1, -1]
    elif start[1] <= stop[1]:
        y_range = [start[1], stop[1] + 1]

    # Part 1
    if part == 1:
        for i in range(*x_range):
            for j in range(*y_range):
                if action == 'on':
                    grid[(i, j)] = True
                elif action == 'off':
                    grid[(i, j)] = False
                elif action == 'toggle':
                    grid[(i, j)] = not grid[(i, j)]
        return grid

    # Part 2
    if part == 2:
        for i in range(*x_range):
            for j in range(*y_range):
                if action == 'on':
                    grid[(i, j)] += 1
                elif action == 'off' and grid[(i, j)] != 0:
                    grid[(i, j)] -= 1
                elif action == 'toggle':
                    grid[(i, j)] += 2
        return grid

with open('day6.txt') as f:
    read_data = f.read().strip().split('\n')
    processed_data = [i.split() for i in read_data]
    # Remove 'through'
    [i.remove(i[-2]) for i in processed_data]
    # Remove 'turn'
    [i.remove(i[0]) for i in processed_data if i[0] == 'turn']
    # Group coordinates and turn into int
    processed_data = [coords_format(i) for i in processed_data]
    grid1 = defaultdict(bool)
    grid2 = defaultdict(int)
    for i in processed_data:
        light_config(*i, grid2, 2)
    print(sum(grid2.values()))
