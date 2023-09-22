with open('day14.txt') as f:
    read_data = f.read().strip().split('\n')
    processed_data = [[[int(i) for i in j.split(',')] for j in k.split(' -> ')] for k in read_data]
    print(processed_data)


class FallingMaterials:
    def __init__(self, data):
        self.data = data
        self.rocks = set()      # Use set for speed
        self.rested = set()
        self.cols = {}
        self.max_depth = 0

    def get_max_depth(self):
        return sorted(self.rocks, key=lambda x: x[0])[-1][0] + 2

    def draw_cave(self):
        for d in self.data:
            for i in range(len(d) - 1):
                self.draw_line(d[i], d[i + 1])

    def draw_line(self, start, stop):
        # Mixed up x and y but it's ok
        y1, x1 = start
        y2, x2 = stop
        if x1 == x2:
            for i in range(max(y1, y2) - min(y1, y2) + 1):
                self.rocks.add((x1, min(y1, y2) + i))
                if min(y1, y2) + i not in self.cols:
                    self.cols[min(y1, y2) + i] = set()
                self.cols[min(y1, y2) + i].add((x1, min(y1, y2) + i))
        else:
            if y1 not in self.cols:
                self.cols[y1] = set()
            for i in range(max(x1, x2) - min(x1, x2) + 1):
                self.rocks.add((min(x1, x2) + i, y1))
                self.cols[y1].add((min(x1, x2) + i, y1))

    def main(self):
        self.draw_cave()
        start = (0, 500)
        while True:
            if self.falling(start) == 'freefall':
                break
        print(len(self.rested))
        # Part 2
        # Continues from part 1
        self.max_depth = self.get_max_depth()
        # Update bottom
        for c in self.cols:
            self.cols[c].add((self.max_depth, c))
            self.rocks.add((self.max_depth, c))
        while True:
            if self.falling2(start) == 'filled':
                break
        print(len(self.rested))

    def falling(self, start):
        x, y = start
        # Nothing below
        if y not in self.cols:
            return 'freefall'
        # Right above the closet rock or sand
        if (x + 1, y) not in self.cols[y]:
            x = min([i[0] for i in self.cols[y] if i[0] - x > 0]) - 1
        # Check 2 sides
        for i in [-1, 1]:
            new = (x + 1, y + i)
            # Keep falling to a side
            if new not in self.rocks and new not in self.rested:
                return self.falling(new)
        # If all 3 below are blocked
        self.rested.add((x, y))
        self.cols[y].add((x, y))

    def falling2(self, start):
        x, y = start
        if (x, y) in self.rested:
            return 'filled'
        # At the bottom
        if y not in self.cols:
            # Expanding bottom
            self.cols[y] = {(self.max_depth, y)}
            self.rocks.add((self.max_depth, y))
            x = self.max_depth - 1
            self.rested.add((x, y))
            self.cols[y].add((x, y))
            return
        if (x + 1, y) not in self.cols[y]:
            x = min([i[0] for i in self.cols[y] if i[0] - x > 0]) - 1
        # Check 2 sides
        for i in [-1, 1]:
            new = (x + 1, y + i)
            if new not in self.rocks and new not in self.rested:
                return self.falling2(new)
        self.rested.add((x, y))
        self.cols[y].add((x, y))


if __name__ == '__main__':
    f = FallingMaterials(processed_data)
    f.main()
