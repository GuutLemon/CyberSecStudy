with open('day6.txt') as f:
    read_data = f.read().strip().split('\n')
    processed_data = [_.split(')') for _ in read_data]
    print(processed_data)


class Orbits():
    def __init__(self, data):
        self.data = data
        self.map = {'COM': (0, 0)}
        self.path = []

    def main(self):
        self.mapping()
        # print(sum([sum(_) for _ in self.map.values()]))   # Part 1
        print(self.cal_path())

    def mapping(self):
        check = ['COM']
        new = []
        while True:
            for c in check:
                for d in self.data:
                    if c == d[0]:
                        x = self.map[d[0]][0]
                        y = self.map[d[0]][1]
                        new.append(d[1])
                        if len(new) == 1:
                            self.map[d[1]] = (x + 1, y)
                        else:
                            # self.map[d[1]] = (x, y + 1)       # Part 1
                            self.map[d[1]] = (x, x + y * len(new))    # Make sure y is unique for each branching paths
            if not new:
                break
            check = new[::]
            new = []

    def cal_path(self):
        you = self.map['YOU']
        san = self.map['SAN']
        print(you, san)
        path1 = self.make_path(you, 0)
        path2 = self.make_path(san, 0)

        path2_y = [i[1] for i in path2]
        for i in path1:
            if i[1] in path2_y:
                stop_y = i[1]
                break

        path1 = self.make_path(you, stop_y)
        path2 = self.make_path(san, stop_y)
        print(path1)
        print(path2)
        return len(path1)-1 + len(path2)-1 + abs(path1[-1][0] - path2[-1][0])

    def make_path(self, coord, stop_y):
        path = []
        while True:
            coord = self.descending(coord)
            path.append(coord)
            if coord[1] == stop_y:
                return path

    def descending(self, coord):
        x, y = coord
        all_coords = self.map.values()
        if (x - 1, y) in all_coords:
            x, y = (x - 1, y)
        else:
            for i in self.map:
                if self.map[i] == (x, y):
                    current = i
                    break
            for d in self.data:
                if d[1] == current:
                    x, y = self.map[d[0]]
                    break
        return x, y


if __name__ == '__main__':
    o = Orbits(processed_data)
    o.main()
