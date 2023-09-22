with open('day9.txt') as f:
    read_data = f.read().strip().split('\n')
    map = [[int(i) for i in j] for j in read_data]

    lowest = []
    lowest_coords = []

    def check_adjacent(map, row, col):
        pos = {}
        # Left
        if col > 0:
            pos[(row, col-1)] = map[row][col - 1]
        # Right
        if col < len(map[0]) - 1:
            pos[(row, col+1)] = map[row][col + 1]
        # Up
        if row > 0:
            pos[(row-1, col)] = map[row - 1][col]
        # Down
        if row < len(map) - 1:
            pos[(row+1, col)] = map[row + 1][col]
        return pos

    for row in range(len(map)):
        for col in range(len(map[0])):
            pos = check_adjacent(map, row, col)
            current_pos = map[row][col]
            if all(current_pos < i for i in pos.values()):
                lowest.append(current_pos)
                lowest_coords.append((row, col))

    risk_levels = [i+1 for i in lowest]
    print(lowest)
    print(lowest_coords)
    print(sum(risk_levels))

    # Part 2
    def check_basin(map, row, col):
        basin = {}
        elevated = []
        pos = check_adjacent(map, row, col)
        current_pos = map[row][col]
        if (row, col) not in basin:
            basin[(row, col)] = current_pos
        #print(basin)
        for p, h in pos.items():
            if current_pos + 1 <= h and h < 9:
                elevated.append(p)
        #print('cow', elevated)
        if len(elevated) == 0:
            #print('cat', basin)
            return basin
        for e in elevated:
            basin.update(check_basin(map, *e))
            #print('dog', basin)
        return basin

    basin_size = []
    for i in lowest_coords:
        basin = check_basin(map, *i)
        basin_size.append(len(basin))
        print(basin)
    print(sorted(basin_size)[-3:])

