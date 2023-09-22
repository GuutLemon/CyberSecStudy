from itertools import product

with open('day17.txt') as f:
    read_data = f.read().strip().split('\n')


class ConwayCube():
    def __init__(self, inp):
        self.inp = inp
        self.grid = {}
        self.directions = self.get_direction()
        self.temp_grid = {}

    def get_direction(self):
        # directions = list(product([-1, 0, 1], repeat=3))   # Part 1
        directions = list(product([-1, 0, 1], repeat=4))
        # directions.remove((0, 0, 0))     # Part 1
        directions.remove((0, 0, 0, 0))
        return directions

    def get_input_grid(self):
        adjacent_cubes = []
        for row in range(len(self.inp)):
            for col in range(len(self.inp[0])):
                # self.grid[(col, row, 0)] = self.inp[row][col]     # Part 1
                self.grid[(col, row, 0, 0)] = self.inp[row][col]
        for c in self.grid:
            for d in self.directions:
                adjacent_cubes.append(tuple(a + b for a, b in zip(c, d)))
        for a in adjacent_cubes:
            if a not in self.grid:
                self.grid[a] = '.'

    def main(self):
        self.get_input_grid()
        self.cal_state()
        # print(self.grid)
        print(list(self.grid.values()).count('#'))

    def cal_state(self):
        for _ in range(6):
            for c in self.grid:
                # print(self.temp_grid)
                adj = self.get_adjacent(c)
                # print(adj)

                if self.grid[c] == '#':
                    if adj.count('#') in [2, 3]:
                        self.temp_grid[c] = '#'
                        # print(c, self.temp_grid[c])
                    else:
                        self.temp_grid[c] = '.'
                        # print(c, self.temp_grid[c], 'b')
                elif self.grid[c] == '.':
                    if adj.count('#') == 3:
                        self.temp_grid[c] = '#'
                        # print(c, self.temp_grid[c])
                    else:
                        self.temp_grid[c] = '.'
                        # print(c, self.temp_grid[c], 'a')
            self.grid = self.temp_grid.copy()
            print('Cycle', _ + 1)

    def get_adjacent(self, c):
        adj = []
        for d in self.directions:
            adjacent_cube = tuple(a + b for a, b in zip(c, d))
            # print(adjacent_cube, c , d)
            if adjacent_cube in self.grid:
                adj.append(self.grid[adjacent_cube])
                # print(self.grid[adjacent_cube], adjacent_cube)
            else:
                adj.append('.')
                self.temp_grid[adjacent_cube] = '.'
        return adj


c = ConwayCube(read_data)
c.main()