with open("day3.txt") as f:
    read_data = f.read().strip().split('\n')


def register_numbers_and_gears():
    num_pos = []
    gear_pos = []
    for i in range(len(read_data)):
        current_num = ''
        num_found = False
        for j in range(len(read_data[0])):
            if read_data[i][j].isdigit():
                if not num_found:
                    num_found = True
                    start_pos = (i, j)
                current_num += read_data[i][j]
            elif read_data[i][j] == "*":
                gear_pos.append((i, j))
            if (num_found and not read_data[i][j].isdigit()) or (num_found and j == len(read_data[0]) - 1):   # Catch number at the end of the line
                num_found = False
                end_pos = (i, j - 1)
                num_pos.append((current_num, start_pos, end_pos))
                current_num = ''
    return num_pos, gear_pos


def check_parts(num, s_pos):
    directions = {(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)}
    adjacent = set()
    for i in range(len(num)):
        (x, y) = (s_pos[0], s_pos[1] + i)
        for d in directions:
            (dx, dy) = (x + d[0], y + d[1])
            if dx < len(read_data) and dy < len(read_data[0]) and not read_data[dx][dy].isdigit():
                adjacent.add(read_data[dx][dy])
    if all(i == '.' for i in adjacent):
        return False
    return True


num_pos, gear_pos = register_numbers_and_gears()
parts_sum = 0
for n in num_pos:
    if check_parts(n[0], n[1]):
        parts_sum += int(n[0])
print(parts_sum)


# Part 2
def check_gears(gear):
    directions = {(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)}
    adjacent = []
    gear_ratios = []
    for d in directions:
        dx, dy = (gear[0] + d[0], gear[1] + d[1])
        if dx < len(read_data) and dy < len(read_data[0]) and read_data[dx][dy].isdigit():
            adjacent.append((dx, dy))
    for n in num_pos:
        for a in adjacent:
            if a in n:  # Gear always be next to head or tail or both of a number because numbers are only max 3 digits
                gear_ratios.append(int(n[0]))
                break   # Prevent duplicate matching both head and tail
    if len(gear_ratios) == 2:
        return gear_ratios[0] * gear_ratios[1]


sum_ratios = 0
for g in gear_pos:
    ratio = check_gears(g)
    if ratio:
        sum_ratios += ratio
print(sum_ratios)