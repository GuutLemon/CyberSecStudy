with open('day3.txt') as f:
    read_data = f.read().strip().split('\n')


class Toboggan():
    def __init__(self):
        self.grid = read_data

    def extend_grid(self):
        max = len(read_data) // len(read_data[0]) * 7 + (len(read_data) % len(read_data[0]))
        self.grid = [i*max for i in read_data]

    def main(self):
        self.extend_grid()
        slopes = [(1, 3), (1, 1), (1, 5), (1, 7), (2, 1)]
        # Part 1
        print(self.sliding(slopes[0]))

        # Part 2
        trees = []
        for slope in slopes:
            trees.append(self.sliding(slope))
        result = 1
        for i in trees:
            result *= i
        print(result)

    def sliding(self, slope):
        mrow, mcol = slope
        count = 0
        row = 0
        col = 0
        while True:
            try:
                row += mrow
                col += mcol
                if self.grid[row][col] == '#':
                    count += 1
            except IndexError:
                return count


t = Toboggan()
t.main()