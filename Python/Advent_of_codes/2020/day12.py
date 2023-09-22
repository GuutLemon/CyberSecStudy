with open('day12.txt') as f:
    read_data = f.read().strip().split('\n')
    moves = [[_[0], int(_[1:])] for _ in read_data]
    print(moves)


def find_location1(lst):
    directions = {'W': (-1, 0), 'N': (0, 1), 'E': (1, 0), 'S': (0, -1)}
    x, y = (0, 0)
    facing = 'E'
    facing_index = 2

    for i in lst:
        # print(i)
        cmd = i[0]
        if cmd in directions:
            dist = i[1]
            for d in range(1, dist + 1):
                x += directions[cmd][0]
                y += directions[cmd][1]
        elif cmd == 'F':
            dist = i[1]
            for d in range(1, dist + 1):
                x += directions[facing][0]
                y += directions[facing][1]
        else:
            rotate = i[1] // 90 % 4
            if cmd == 'R':
                facing_index = (facing_index + rotate) % 4
            else:
                facing_index = (facing_index - rotate) % 4
            facing = list(directions.keys())[facing_index]
            # print(facing_index)
        # print(x, y)
    return abs(x) + abs(y)

# print(find_location1(moves))


def find_location2(lst):
    directions = {'W': (-1, 0), 'N': (0, 1), 'E': (1, 0), 'S': (0, -1)}
    x, y = (0, 0)
    facing = 'E'
    facing_index = 2
    wx, wy = (10, 1)

    for i in lst:
        print(i)
        print(wx, wy)
        cmd = i[0]
        if cmd in directions:
            dist = i[1]
            for d in range(1, dist + 1):
                wx += directions[cmd][0]
                wy += directions[cmd][1]
        elif cmd == 'F':
            dist = i[1]
            for d in range(1, dist + 1):
                x += wx
                y += wy
        else:
            rotate = i[1] // 90 % 4
            if cmd == 'R':
                current_facing_index = (facing_index + rotate) % 4
            else:
                current_facing_index = (facing_index - rotate) % 4
            # print((current_facing_index, facing_index))

            if abs(facing_index - current_facing_index) == 2:
                wx, wy = -wx, -wy
            elif abs(facing_index - current_facing_index) % 2 == 1:
                if (current_facing_index == facing_index + 1) or (current_facing_index == 0 and facing_index == 3):
                    wx, wy = wy, -wx
                elif (current_facing_index == facing_index - 1) or (current_facing_index == 3 and facing_index == 0):
                    wx, wy = -wy, wx

            facing_index = current_facing_index
            facing = list(directions.keys())[facing_index]
            print(wx, wy)

        # print(x, y)
    return abs(x) + abs(y)

print(find_location2(moves))
