def find_HQ(instructions):
    directions = {'U': (0, 1), 'R': (1, 0), 'D': (0, -1), 'L': (-1, 0)}
    current_dir_indx = 0
    current_pos = (0, 0)
    visited = [(0, 0)]
    HQ_found = False

    for instr in instructions:
        if instr[0] == 'R':
            current_dir_indx = (current_dir_indx + 1) % len(directions)
        else:
            current_dir_indx = (current_dir_indx - 1) % len(directions)
        current_dir = list(directions.keys())[current_dir_indx]
        for i in range(int(instr[1:])):
            current_pos = tuple(map(sum, zip(current_pos, directions[current_dir])))

            # Part 2
            if not HQ_found:
                if current_pos not in visited:
                    visited.append(current_pos)
                else:
                    HQ_found = True
                    HQ_loc = current_pos

    return abs(current_pos[0]) + abs(current_pos[1]), abs(HQ_loc[0]) + abs(HQ_loc[1])

if __name__ == '__main__':
    with open('day1.txt') as f:
        instructions = f.read().strip().split(', ')
    solve = find_HQ(instructions)
    print('Part 1: ', solve[0])
    print('Part 2: ', solve[1])
