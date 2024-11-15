import re


def viable_pairs(grid):
    count = 0
    for f in grid:
        if grid[f]['used'] > 0:
            for check in grid:
                    if grid[f]['used'] <= grid[check]['avail']:
                        count += 1
    return count


if __name__ == '__main__':
    with open('day22.txt') as f:
        files = f.read().strip().split('\n')
        pattern = re.compile(r'x(\d+)-y(\d+)')
        grid = dict()
        for f in files[2:]:
            file_name = tuple(int(_) for _ in re.findall(pattern, f)[0])
            f = f.split()
            grid[file_name] = {'size': int(f[1][:-1]), 'used': int(f[2][:-1]), 'avail': int(f[3][:-1]), 'use%': int(f[4][:-1])}

    print('Part 1: ',viable_pairs(grid))