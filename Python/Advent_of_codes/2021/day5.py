from collections import defaultdict

with open('day5.txt') as f:
    read_data = f.read().strip().split('\n')
    processed_data = [[eval('(' + i + ')') for i in j.split(' -> ')] for j in read_data]
    print(processed_data)

    grid = defaultdict(int)
    for l in processed_data:
        x1 = l[0][0]
        y1 = l[0][1]
        x2 = l[1][0]
        y2 = l[1][1]
        if x1 == x2:
            min_y = min(y1, y2)
            distance = abs(y1 - y2)
            for i in range(min_y, min_y + distance + 1):
                grid[x1, i] += 1
        elif y1 == y2:
            min_x = min(x1, x2)
            distance = abs(x1 - x2)
            for i in range(min_x, min_x + distance + 1):
                grid[i, y1] += 1

        # Part 2
        elif abs(x1 - x2) == abs(y1 - y2):
            #print(l)
            # Get positive or negative distances
            _x = (x1 - x2)//abs(x1 - x2)
            _y = (y1 - y2)//abs(y1 - y2)
            distance = abs(x1 - x2)
            for i in range(distance + 1):
                #print(x1 - i*_x, y1 - i*_y)
                grid[x1 - i*_x, y1 - i*_y] += 1

    #print(grid)
    count = 0
    for v in grid.values():
        if v > 1:
            count += 1
    print(count)

