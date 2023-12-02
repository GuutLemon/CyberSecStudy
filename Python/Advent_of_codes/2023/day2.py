import re

with open("day2.txt") as f:
    read_data = f.read().strip().split('\n')
    # games = [l.split(': ')[1].split('; ') for l in read_data]


# Part 1
def regex_compare(line):
    max_red = 12
    max_green = 13
    max_blue = 14
    p_r = '(\d\d?)(?: red)'
    p_g = '(\d\d?)(?: green)'
    p_b = '(\d\d?)(?: blue)'
    r = [int(i) for i in re.findall(p_r, line)]
    g = [int(i) for i in re.findall(p_g, line)]
    b = [int(i) for i in re.findall(p_b, line)]
    if all(i <= max_red for i in r) and\
            all(i <= max_green for i in g) and\
            all(i <= max_blue for i in b):
        return True
    return False

result = 0
for game in range(len(read_data)):
    if regex_compare(read_data[game]):
        result += game + 1
print('Part 1:', result)

# Part 2
def regex_min_cubes(line):
    p_r = '(\d\d?)(?: red)'
    p_g = '(\d\d?)(?: green)'
    p_b = '(\d\d?)(?: blue)'
    r = [int(i) for i in re.findall(p_r, line)]
    g = [int(i) for i in re.findall(p_g, line)]
    b = [int(i) for i in re.findall(p_b, line)]
    return max(r) * max(g) * max(b)

result = 0
for game in range(len(read_data)):
    result += regex_min_cubes(read_data[game])
print('Part 2:', result)