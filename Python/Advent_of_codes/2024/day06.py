def get_starting_pos(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '^':
                return i, j

def find_path(grid, starting_pos):
    i, j = starting_pos
    path = {(i, j)}
    path_2 = {(i, j, 'U')}
    directions = {'U': (-1, 0, 'R'), 'R': (0, 1, 'D'), 'D': (1, 0, 'L'), 'L': (0, -1, 'U')}
    current_dir = 'U'
    while True:
        x, y = i + directions[current_dir][0], j + directions[current_dir][1]
        if x < 0 or y < 0:
            return path
        try:
            if grid[x][y] == '#':
                current_dir = directions[current_dir][2]
            else:
                i, j = x, y
                path.add((i, j))
                if (i, j, current_dir) in path_2:
                    return 'loop'
                path_2.add((i, j, current_dir))
        except IndexError:
            return path

def find_loops(grid, path, starting_pos):
    count = 0
    for tile in path:
        i, j = tile[0], tile[1]
        grid[i][j] = '#'
        if find_path(grid, starting_pos) == 'loop':
            count += 1
        grid[i][j] = '.'
    return count


if __name__ == '__main__':
    with open('day06.txt') as f:
        INP = f.read().strip().split('\n')
        INP = [list(_) for _ in INP]

    start = get_starting_pos(INP)
    path = find_path(INP, start)
    print('Part 1: ', len(path))
    path.remove(start)
    print('Part 2: ', find_loops(INP, path, start))