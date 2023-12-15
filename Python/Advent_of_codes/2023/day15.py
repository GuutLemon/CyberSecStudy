import re
from collections import defaultdict

with open('day15.txt') as f:
    read_data = f.read().strip().split(',')

def hashing(inp):
    value = 0
    for char in inp:
        code = ord(char)
        value += code
        value *= 17
        value = value % 256
    return value

def sort_box(data):
    boxes = defaultdict(dict)
    p = re.compile(r'(\w+)[-=]')
    for i in data:
        lable = p.findall(i)[0]
        box = hashing(lable)
        if '=' in i:
            boxes[box].update({lable: int(i[-1])})
        elif '-' in i and lable in boxes[box]:
            del boxes[box][lable]
    return boxes

def cal_powr(boxes):
    total = 0
    for b in boxes:
        lens = boxes[b]
        for i in range(len(lens)):
            powr = (b + 1) * (i + 1) * lens[list(lens.keys())[i]]
            total += powr
    return total


print('Part 1:', sum(hashing(i) for i in read_data))
boxes = sort_box(read_data)
print('Part 2:', cal_powr(boxes))

