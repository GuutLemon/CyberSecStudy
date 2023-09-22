with open('day3.txt') as f:
    read_data = f.read().strip().split('\n')
    processed_data = [_.split(',') for _ in read_data]
    print(processed_data)


def path_finding(cmds):
    directions = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
    x, y = (0, 0)
    path = []
    for i in cmds:
        distance = int(i[1:])
        cmd = i[0]
        for d in range(distance):
            x += directions[cmd][0]
            y += directions[cmd][1]
            path.append((x, y))
    return path


def find_closest_intersection(data):
    paths = {}
    for i in range(1, 3):
        paths[i] = set(path_finding(data[i-1]))
    intersections = paths[1] & paths[2]
    # Part 1
    # sums = []
    # for i in intersections:
    #     sums.append(abs(i[0]) + abs(i[1]))
    # return min(sums)
    return intersections
# print(find_closest_intersection(processed_data))


intersections = find_closest_intersection(processed_data)
def path_finding2(cmds, intersections):
    directions = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
    x, y = (0, 0)
    steps = 0
    steps_to_intersection = {}
    for i in cmds:
        distance = int(i[1:])
        cmd = i[0]
        for d in range(distance):
            steps += 1
            x += directions[cmd][0]
            y += directions[cmd][1]
            if (x, y) in intersections:
                steps_to_intersection[(x, y)] = steps
    # print(steps_to_intersection)
    return steps_to_intersection


def find_closest_path(data, intersections):
    paths = {}
    for i in range(1, 3):
        paths[i] = path_finding2(data[i - 1], intersections)
    total_steps = []
    for p in paths[1]:
        total_steps.append(paths[1][p] + paths[2][p])
    return min(total_steps)


print(find_closest_path(processed_data, intersections))
