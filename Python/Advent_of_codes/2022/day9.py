# # def tail_movement(head_coord, tail_coord, tail_path):
# def tail_movement(head_coord, tail_coord):
#     x_displace = abs(head_coord[0] - tail_coord[0])
#     y_displace = abs(head_coord[1] - tail_coord[1])
#     if x_displace <= 1 and y_displace <= 1:
#         return tail_coord #, tail_path
#     elif x_displace > 1:
#         if head_coord[0] > tail_coord[0]:
#             tail_coord[0] += 1
#         else:
#             tail_coord[0] -= 1
#         tail_coord[1] = head_coord[1]
#         #tail_path.add((tail_coord[0], tail_coord[1]))
#         return tail_coord #, tail_path
#     elif y_displace > 1:
#         if head_coord[1] > tail_coord[1]:
#             tail_coord[1] += 1
#         else:
#             tail_coord[1] -= 1
#         tail_coord[0] = head_coord[0]
#         #tail_path.add((tail_coord[0], tail_coord[1]))
#         return tail_coord #, tail_path
#
#
# def rope_tracing(moves):
#     tail_path = set()
#     head_coord = [0, 0]
#     tail_coords = [[0, 0] for _ in range(9)]
#     x_moves = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
#     y_moves = {'U': 1, 'D': -1, 'L': 0, 'R': 0}
#     # Part 1
#     for move in moves:
#         cmd = move[0]
#         distance = move[1]
#         for _ in range(distance):
#             head_coord = [head_coord[0] + x_moves[cmd], head_coord[1] + y_moves[cmd]]
#             # Part 1
#             #tail_coord, tail_path = tail_movement(head_coord, tail_coord, tail_path)
#
#             # Part 2
#             tail_coords[0] = tail_movement(head_coord, tail_coords[0])
#             tail_path.add((tail_coords[-1][0], tail_coords[-1][1]))
#             for i in range(1, 9):
#                 tail_coords[i] = tail_movement(tail_coords[i-1], tail_coords[i])
#             tail_path.add((tail_coords[-1][0], tail_coords[-1][1]))
#         print(tail_coords)
#     return len(list(tail_path))
#

# Redone
with open('day9.txt') as f:
    read_data = f.read().strip().split('\n')
    processed_data = [[int(i) if i.isdigit() else i for i in j.split()] for j in read_data]
    print(processed_data)


class Rope:
    def __init__(self, cmds):
        self.cmds = cmds
        self.directions = {
            'R': (1, 0),
            'L': (-1, 0),
            'U': (0, 1),
            'D': (0, -1)
        }
        self.tail = (0, 0)

    def main(self):
        print(len(set(self.moving_knots())))

    def first_knot_move(self, c, knot):
        cmd = c[0]
        x, y = knot
        return x + self.directions[cmd][0], y + self.directions[cmd][1]

    def next_knot_move(self, first_knot, next_knot):
        x1, y1 = first_knot
        x2, y2 = next_knot
        dist = (abs(x1 - x2), abs(y1 - y2))
        if all(d <= 1 for d in dist):
            return x2, y2
        elif dist[0] == 2 and dist[1] <= 1:
            return x1 - 1*(x1 > x2) + 1*(x1 < x2), y1
        elif dist[1] == 2 and dist[0] <= 1:
            return x1, y1 - 1*(y1 > y2) + 1*(y1 < y2)
        # Part 2
        # Diagonal, took a while to find out because part 1 doesn't have this
        else:
            return x1 - 1*(x1 > x2) + 1*(x1 < x2), y1 - 1*(y1 > y2) + 1*(y1 < y2)

    def moving_knots(self):
        path = [self.tail]
        knots = [(0, 0) for _ in range(10)]     # range(2) for part 1
        for c in self.cmds:
            dist = c[1]
            for _ in range(dist):
                knots[0] = self.first_knot_move(c, knots[0])
                knots[1] = self.next_knot_move(knots[0], knots[1])

                # Part 2
                if len(knots) > 2:
                    for i in range(1, len(knots) - 1):
                        knots[i + 1] = self.next_knot_move(knots[i], knots[i + 1])

                self.tail = knots[-1]
                path.append(self.tail)
        return path


if __name__ == '__main__':
    r = Rope(processed_data)
    r.main()
