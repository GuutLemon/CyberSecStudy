with open('day2.txt') as f:
    boxes = f.read().strip().split('\n')
    boxes = [sorted([int(i) for i in b.split('x')]) for b in boxes]

# Part 1
def total_area(boxes):
    area = 0
    for b in boxes:
        min_side = b[0]*b[1]
        area += 2*b[0]*b[1] + 2*b[2]*b[1] + 2*b[2]*b[0] + min_side
    return area

# Part 2
def total_ribbon(boxes):
    length = 0
    for b in boxes:
        min_perimeter = 2*b[0] + 2*b[1]
        volume = b[0]*b[1]*b[2]
        length += min_perimeter + volume
    return length


print(total_area(boxes))
print(total_ribbon(boxes))

