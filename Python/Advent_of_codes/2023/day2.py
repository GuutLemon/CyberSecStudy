import re

with open("day2.txt") as f:
    read_data = f.read().strip().split('\n')
    # games = [l.split(': ')[1].split('; ') for l in read_data]


def regex_check(line):
    max_red = 12
    max_green = 13
    max_blue = 14
    check = False
    p_r = '(\d+)(?: red)'
    p_g = '(\d+)(?: green)'
    p_b = '(\d+)(?: blue)'
    r = [int(i) for i in re.findall(p_r, line)]
    g = [int(i) for i in re.findall(p_g, line)]
    b = [int(i) for i in re.findall(p_b, line)]
    if all(i <= max_red for i in r) and\
            all(i <= max_green for i in g) and\
            all(i <= max_blue for i in b):
        check = True
    return check, max(r) * max(g) * max(b)


result1 = 0
result2 = 0
for game in range(len(read_data)):
    if regex_check(read_data[game])[0]:
        result1 += game + 1
    result2 += regex_check(read_data[game])[-1]
print('Part 1:', result1, '\nPart 2:', result2)