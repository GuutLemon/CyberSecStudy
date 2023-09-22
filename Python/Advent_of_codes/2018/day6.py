from collections import defaultdict, Counter

with open('day6.txt') as f:
    read_data = f.read().strip().split('\n')
    processed_data = set(eval('(' + _ + ')') for _ in read_data)
    print(processed_data)


# class FillAreas:
#     def __init__(self, points):
#         self.points = points
#         self.areas = {}
#         for p in self.points:
#             self.areas[p] = {p}
#         print(self.areas)
#         self.checking = defaultdict(set)
#
#     def mapping(self):
#         for i in range(1, 401):
#             for p in self.points:
#                 self.get_circumference(p, i)
#             self.expanding()
#
#     def get_circumference(self, point, radius):
#         x, y = point
#         i = 0
#         for nx in range(x - radius, x):
#             self.checking[(nx, y + i)].add(point)
#             self.checking[(nx, y - i)].add(point)
#             i += 1
#         i = 0
#         for nx in range(x, x + radius + 1):
#             self.checking[(nx, y - radius + i)].add(point)
#             self.checking[(nx, y + radius - i)].add(point)
#             i += 1
#
#     def expanding(self):
#         for point in self.checking:
#             if point not in self.areas and point not in self.points:
#                 self.areas[point] = self.checking[point]
#         self.checking = defaultdict(set)
#
#
# if __name__ == '__main__':
#     solve = FillAreas(processed_data)
#     solve.mapping()
#     result = []
#     for v in solve.areas.values():
#         if len(v) == 1:
#             result.append(list(v)[0])
#     result = Counter(result)
#     print(result)
## Inefficient
## No way of knowing stoping point
## But the result was still true


class FillAreas:
    def __init__(self, points):
        self.points = points
        self.areas = {p: p for p in self.points}
        self.max_x = sorted(self.points, key=lambda x: x[0])[-1][0]
        self.max_y = sorted(self.points, key=lambda x: x[1])[-1][1]
        self.min_x = sorted(self.points, key=lambda x: x[0])[0][0]
        self.min_y = sorted(self.points, key=lambda x: x[0])[0][1]

    def cal_distance(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    def find_min_distances(self):
        for x in range(self.min_x, self.max_x):
            for y in range(self.min_y, self.max_y):
                dist = {}
                for p in self.points:
                    if (x, y) is p:
                        continue
                    dist[self.cal_distance((x, y), p)] = p
                min_dist = min(dist.keys())
                if list(dist).count(min_dist) == 1:
                    self.areas[(x, y)] = dist[min_dist]


if __name__ == '__main__':
    solve = FillAreas(processed_data)
    solve.find_min_distances()
    result1 = Counter(solve.areas.values())
    print(result1)