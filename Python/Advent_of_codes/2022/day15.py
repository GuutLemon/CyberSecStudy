import re

with open('day15.txt') as f:
    read_data = f.read().strip().split('\n')
    print(read_data)
    processed_data = []
    for i in read_data:
        processed_data.append([int(_) for _ in re.findall(r'=(-?\d+)', i)])
    print(processed_data)


class Beacons:
    def __init__(self, data):
        self.data = data
        self.radius = {}
        self.beacons = set([tuple(_[2:]) for _ in self.data])   # Remember to turn lists to tuples before adding to set

    def main(self):
        self.cal_radius()
        print(len(self.find_pos()))
        print(self.find_beacon())

    def cal_radius(self):
        for d in self.data:
            self.radius[(d[0], d[1])] = abs(d[0] - d[2]) + abs(d[1] - d[3])

    # Part 1
    def find_pos(self):
        y = 2000000
        pos = set()
        for s in self.radius:
            intersections = self.find_intersections(s, y)
            if intersections:
                for i in range(intersections[0], intersections[1] + 1):
                    if (i, y) not in self.beacons:
                        pos.add(i)
        return pos

    def find_intersections(self, s, y):
        x = s[0]
        dist = self.radius[s] - abs(y - s[1])
        if dist == 0:
            return x, x + 1
        elif dist > 0:
            # print(dist, self.radius[s], y, s[1])
            left = x - dist
            right = x + dist
            return left, right

    # Part 2
    def find_beacon(self):
        max_y = 4000000
        for y in range(max_y + 1):
            pos = []    # Using list because we will have to sort it
            for s in self.radius:
                intersections = self.find_ranges(s, y)
                if intersections:
                    pos.append(intersections)
            x = self.result(pos)
            if x:
                return x * 4000000 + y

    def find_ranges(self, s, y):
        x = s[0]
        max_x = 4000000
        dist = self.radius[s] - abs(y - s[1])
        if dist == 0:
            if x > max_x:
                return max_x, max_x
            elif x < 0:
                return 0, 0
            return x, x
        elif dist > 0:
            left = x - dist
            right = x + dist
            result = [left, right]
            for i in range(len(result)):
                if result[i] > max_x:
                    result[i] = max_x
                elif result[i] < 0:
                    result[i] = 0
            return result[0], result[1]

    def result(self, pos):
        combined_ranges = []
        for start, end in sorted(pos):
            if combined_ranges and start <= combined_ranges[-1][1] + 1:     # (1 (2 2) 3), (1 2)(3 4)
                combined_ranges[-1] = (combined_ranges[-1][0], max(end, combined_ranges[-1][1]))    # not (1 (2 3) 4)
            else:
                combined_ranges.append((start, end))
        missing_num = []
        check = combined_ranges[0][0]
        if len(combined_ranges) > 1:
            for start, end in combined_ranges:
                if check < start:
                    missing_num.extend(range(check, start))
                check = end + 1
            return missing_num[0]


if __name__ == '__main__':
    s = Beacons(processed_data)
    s.main()