def shortest_path(instr):
    directions = {'nw': (1, 0.5),
                  'n': (0, 1),
                  'ne': (-1, 0.5),
                  'se': (-1, -0.5),
                  's': (0, -1),
                  'sw': (1, -0.5)}
    path = set()
    current_pos = (0, 0)
    for i in instr:
        current_pos = tuple(map(sum, zip(current_pos, directions[i])))
        path.add(current_pos)
    # print(current_pos)
    # if abs(current_pos[0]) / 2 < abs(current_pos[1]):
    #     min_dist = abs(current_pos[0]) + abs(current_pos[1]) - abs(current_pos[0]) / 2
    #     dist = [abs(i[0]) + abs(i[1]) - abs(i[0]) / 2 for i in path]
    #     furthest = int(max(dist))
    # else:
    #     min_dist = current_pos[0]
    #     dist = [abs(i[0]) for i in path]
    #     furthest = max(dist)
    return int(min_dist), furthest


if __name__ == '__main__':
    with open('day11.txt') as f:
        INP = f.read().strip().split(',')
        # INP = 'se,sw,se,sw,sw,se,sw,se,sw,s,s,nw,nw,n'.split(',')

    solved = shortest_path(INP)
    print('Part 1: ', solved[0])
    print('Part 2: ', solved[1])
