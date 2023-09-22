with open('day3.txt') as f:
    read_data = f.read().strip().replace(',', ' '). replace('x', ' ').replace(':', '').split('\n')
    processed_data = [i[i.rfind('@ ') + 2:] for i in read_data]
    processed_data = [[int(i) for i in j.split()] for j in processed_data ]
    print(processed_data)


grid = {}
def mapping(grid, start, sides):
    for r in range(sides[1]):
        for c in range(sides[0]):
            if (start[0] + c, start[1] + r) in grid:
                grid[(start[0] + c, start[1] + r)] = False
            else:
                grid[(start[0] + c, start[1] + r)] = True
            yield start[0] + c, start[1] + r


patches = {}
for i, j in enumerate(processed_data):
    start = j[0], j[1]
    sides = j[2], j[3]
    patches[i+1] = set(mapping(grid, start, sides))

count = 0
for i in grid:
    if not grid[i]:
        count += 1
print(count)

for i, v in patches.items():
    if all(grid[p] for p in v):
        print(i)
        exit(0)
