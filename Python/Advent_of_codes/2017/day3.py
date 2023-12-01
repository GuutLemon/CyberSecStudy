INP = 265149

class DrawSpiral:
    def __init__(self, size):
        self.size = size
        self.grid = {(0, 0): 1}
        self.current_direction = "R"
        self.current_cell = (0, 0)
        self.directions = {"U": (0, 1), "R": (1, 0), "D": (0, -1), "L": (-1, 0)}
    # First default number is 1 at (0, 0), the program starts at number 2 at (1, 0)

    def count_adjacent(self):
        directions = {(0, 1), (1, 0), (0, -1), (-1, 0)}
        count = 0
        for d in directions:
            x = self.current_cell[0] + d[0]
            y = self.current_cell[1] + d[1]
            if (x, y) in self.grid.keys():
                count += 1
        return count

    def check_direction(self):
        turn_left = {"R": "U", "U": "L", "L": "D", "D": "R"}
        if self.count_adjacent() == 1:
            self.current_direction = turn_left[self.current_direction]
        # Direction only changes when current_cell is over the edge and only next to 1 other cell

    def draw_grid(self):
        if self.size < 2:
            return "Invalid size"   # Program only starts at 2
        for i in range(2, self.size + 1):
            self.check_direction()
            self.current_cell = tuple(map(sum, zip(self.current_cell, self.directions[self.current_direction])))
            self.grid[self.current_cell] = i
        return self.grid

# Part 2
class AddValues:
    def __init__(self, grid, inp):
        self.grid = grid
        self.inp = inp
        self.values = {1: 1}
        self.current_value = 1

    def cal_current_value(self, current_cell):
        directions = {(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)}
        val_sum = 0
        for d in directions:
            (x, y) = tuple(map(sum, zip(current_cell, d)))
            # Check for valid cells and written cells then add all values of written cells
            if (x, y) in self.grid and self.grid[(x, y)] in self.values:
                val_sum += self.values[self.grid[(x, y)]]
        return val_sum

    def map_value(self):
        for i in list(self.grid)[1:]:   # Starts at 2
            self.current_value = self.cal_current_value(i)
            self.values[self.grid[i]] = self.current_value

            if self.current_value > self.inp:
                return self.current_value


if __name__ == '__main__':
    draw = DrawSpiral(INP)
    grid = draw.draw_grid()
    # Part 1
    steps = sum([abs(i) for i in list(grid.keys())[-1]])
    print(steps)
    # Part 2
    add = AddValues(grid, INP)
    print(add.map_value())