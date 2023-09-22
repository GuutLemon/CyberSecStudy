with open('day11.txt') as f:
    read_data = f.read().strip().split('\n')
    grid = [[int(i) for i in j] for j in read_data]


class Flashes():
    def __init__(self, grid):
        self.grid = grid

    def run(self):
        total_flashes = []
        # Part 1
        # for _ in range(100):

        # Part 2
        i = 0
        while True:
            i += 1
            count = self.count_flashes(self.grid)
            if count == 100:
                # print(self.grid)
                return i

        #     # print(_)
        #     for i in self.grid:
        #         # print(i)
        #     total_flashes.append(count)
        # return sum(total_flashes)

    def count_flashes(self, grid):
        above9 = []
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                self.grid[row][col] += 1
                if self.grid[row][col] > 9:
                    above9.append((row, col))
                    self.grid[row][col] = 0
        self.recursive(above9)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if self.grid[row][col] == 0:
                    count += 1
        return count

    def recursive(self, above9):
        for i in above9:
            self.add_adjacents(*i)
        above9 = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if self.grid[row][col] > 9:
                    above9.append((row, col))
                    self.grid[row][col] = 0
        if len(above9) == 0:
            return
        self.recursive(above9)

    def add_adjacents(self, row, col):
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr <= len(grid) - 1 and 0 <= nc <= len(grid[0]) - 1:
                self.grid[nr][nc] += 1*(self.grid[nr][nc] > 0)
        return


f = Flashes(grid)
print(f.run())
