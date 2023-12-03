with open("day3.txt") as f:
    read_data = f.read().strip().split('\n')


def register_numbers_and_gears(data):
    num_pos = []
    gear_pos = []
    for i in range(len(data)):
        current_num = ''
        num_found = False
        for j in range(len(data[0])):
            if data[i][j].isdigit():
                if not num_found:
                    num_found = True
                    start_pos = (i, j)
                current_num += data[i][j]
            elif data[i][j] == "*":
                gear_pos.append((i, j))
            if (num_found and not data[i][j].isdigit()) or (num_found and j == len(data[0]) - 1):   # Catch number at the end of the line
                num_found = False
                end_pos = (i, j - 1)
                num_pos.append((current_num, start_pos, end_pos))
                current_num = ''
    return num_pos, gear_pos


def check_parts(num, s_pos, data):
    directions = {(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)}
    adjacent = set()
    for i in range(len(num)):
        (x, y) = (s_pos[0], s_pos[1] + i)
        for d in directions:
            (dx, dy) = (x + d[0], y + d[1])
            if dx < len(data) and dy < len(data[0]) and not data[dx][dy].isdigit():
                adjacent.add(data[dx][dy])
    if all(i == '.' for i in adjacent):
        return False
    return True


num_pos, gear_pos = register_numbers_and_gears(read_data)
parts_sum = 0
for n in num_pos:
    if check_parts(n[0], n[1], read_data):
        parts_sum += int(n[0])
print(parts_sum)


# Part 2
def check_gears(num_pos, gear, data):
    directions = {(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)}
    adjacent = []
    gear_ratios = []
    for d in directions:
        dx, dy = (gear[0] + d[0], gear[1] + d[1])
        if dx < len(data) and dy < len(data[0]) and data[dx][dy].isdigit():
            adjacent.append((dx, dy))
    for n in num_pos:
        for a in adjacent:
            if a in n:  # Gear always be next to head or tail or both of a number
                gear_ratios.append(int(n[0]))
                break   # Prevent duplicate matching both head and tail
    if len(gear_ratios) == 2:
        return gear_ratios[0] * gear_ratios[1]


sum_ratios = 0
for g in gear_pos:
    ratio = check_gears(num_pos, g, read_data)
    if ratio:
        sum_ratios += ratio
print(sum_ratios)