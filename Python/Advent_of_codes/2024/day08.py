def get_pos(grid):
    pos = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            tile = grid[i][j]
            if tile != '.':
                if tile not in pos:
                    pos[tile] = [(i, j)]
                else:
                    pos[tile].append((i, j))
    return pos

def count_antinodes(grid, part=1):
    antinodes = set()
    antennas_pos = get_pos(grid)
    in_grid = lambda node: all(0 <= x < len(grid) for x in node)
    for a in antennas_pos.values():
        for i in range(len(a) - 1):
            for j in range(i + 1, len(a)):
                dist = a[j][0] - a[i][0], a[j][1] - a[i][1]
                up = a[i][0], a[i][1]
                down = a[j][0], a[j][1]
                repeat = 1
                if part == 2:
                    repeat = len(grid)
                    antinodes.add(a[i])
                    antinodes.add(a[j])
                for _ in range(repeat):
                    up = up[0] - dist[0], up[1] - dist[1]
                    down = down[0] + dist[0], down[1] + dist[1]
                    if in_grid(up):
                        antinodes.add(up)
                    if in_grid(down):
                        antinodes.add(down)
                    if not in_grid(up) and not in_grid(down):
                        break
    return len(antinodes)


if __name__ == '__main__':
    with open('day08.txt') as f:
        INP = f.read().strip().split('\n')

    print('Part 1: ', count_antinodes(INP, 1))
    print('Part 2: ', count_antinodes(INP, 2))