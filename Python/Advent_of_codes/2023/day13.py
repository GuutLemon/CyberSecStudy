with open('day13.txt') as f:
    read_data = f.read().strip().split('\n\n')

mountains = (i.split('\n') for i in read_data)

# Check if 2 lines have less than 1 different char
def compare_lines(a: int, b: int, m: list, direction: str) -> int:
    diff = 0
    if direction == 'r':
        for i in range(len(m[0])):
            if m[a][i] != m[b][i]:
                diff += 1
            if diff > 1:
                return 2
    else:
        c1 = [m[i][a] for i in range(len(m))]
        c2 = [m[i][b] for i in range(len(m))]
        for j in range(len(m)):
            if c1[j] != c2[j]:
                diff += 1
            if diff > 1:
                return 2
    return diff

# Check till the end of grid if it has less than 1 different pair
def check_mirror(a: int, b: int, m: list, direction: str) -> int:
    diff = 0
    if direction == 'r':
        while a > 0 and b < len(m) - 1:
            a -= 1
            b += 1
            diff += compare_lines(a, b, m, direction)
            if diff > 1:
                return 2
    else:
        while a > 0 and b < len(m[0]) - 1:
            a -= 1
            b += 1
            diff += compare_lines(a, b, m, direction)
            if diff > 1:
                return 2
    return diff

def locate_mirror(m):
    for i in range(len(m) - 1):
        # print(m[i], m[i + 1], compare_lines(i, i + 1, m, 'r'))
        if compare_lines(i, i + 1, m, 'r') == 0 and check_mirror(i, i + 1, m, 'r') == 0:
            return (i + 1) * 100
    for j in range(len(m[0]) - 1):
        # c1 = [m[i][j] for i in range(len(m))]
        # c2 = [m[i][j + 1] for i in range(len(m))]
        # print(c1 , c2 , compare_lines(j, j + 1 , m, 'c'))
        if compare_lines(j, j + 1 , m, 'c') == 0 and check_mirror(j, j + 1 , m, 'c') == 0:
            return j + 1

def locate_fixed_mirror(m):
    for i in range(len(m) - 1):
        if compare_lines(i, i + 1, m, 'r') == 0 and check_mirror(i, i + 1, m, 'r') == 1:
            return (i + 1) * 100
        elif compare_lines(i, i + 1, m, 'r') == 1 and check_mirror(i, i + 1, m, 'r') == 0:
            return (i + 1) * 100
    for j in range(len(m[0]) - 1):
        if compare_lines(j, j + 1 , m, 'c') == 0 and check_mirror(j, j + 1 , m, 'c') == 1:
            return j + 1
        elif compare_lines(j, j + 1 , m, 'c') == 1 and check_mirror(j, j + 1 , m, 'c') == 0:
            return j + 1

total_1 = 0
total_2 = 0
for m in mountains:
    total_1 += locate_mirror(m)
    total_2 += locate_fixed_mirror(m)
print('Part 1:', total_1)
print('Part 2:', total_2)