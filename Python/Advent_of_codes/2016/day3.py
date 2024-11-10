def count_valid(triangles, part):
    valid = 0
    if part == 2:
        ungrouped_triangles = [triangles[i][j] for j in range(3) for i in range(len(triangles))]
        triangles = []
        t = []
        for i in range(len(ungrouped_triangles)):
            t.append(ungrouped_triangles[i])
            if (i + 1) % 3 == 0:
                triangles.append(t)
                t = []

    for t in triangles:
        if all(t[comb[0]] + t[comb[1]] > t[comb[2]] for comb in [(0, 1, 2), (0, 2, 1), (1, 2, 0)]):
            valid += 1
    return valid


if __name__ == '__main__':
    with open('day3.txt') as f:
        triangles = f.read().strip().split('\n')
        triangles = [_.split() for _ in triangles]
        triangles = [[int(i) for i in j] for j in triangles]
    print('Part 1: ', count_valid(triangles, 1))
    print('Part 2: ', count_valid(triangles, 2))