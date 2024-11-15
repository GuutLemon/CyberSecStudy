class MapRoom:
    def __init__(self, first_row, n_row):
        self.grid = [first_row]
        self.n_row = n_row - 1
        self.trap_conditions = {'^^.', '.^^', '^..', '..^'}

    def print_grid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                print(self.grid[i][j], end='')
            print('')

    def count_safe_tiles(self):
        count = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == '.':
                    count += 1
        return count

    def make_tile(self, tile_index):
        left_index = tile_index - 1
        right_index = tile_index + 1
        if left_index < 0:
            left = '.'
            right = self.grid[-1][right_index]
        elif right_index >= len(self.grid[-1]):
            left = self.grid[-1][left_index]
            right = '.'
        else:
            left = self.grid[-1][left_index]
            right = self.grid[-1][right_index]
        middle = self.grid[-1][tile_index]
        checked_titles = left + middle + right
        if checked_titles in self.trap_conditions:
            return '^'
        return '.'

    def make_map(self):
        for i in range(self.n_row):
            new_row = ''
            for i in range(len(self.grid[-1])):
                new_tile = self.make_tile(i)
                new_row += new_tile
            self.grid.append(new_row)


if __name__ == '__main__':
    first_row = '......^.^^.....^^^^^^^^^...^.^..^^.^^^..^.^..^.^^^.^^^^..^^.^.^.....^^^^^..^..^^^..^^.^.^..^^..^^^..'
    room = MapRoom(first_row, 40)
    room.make_map()
    # room.print_grid()
    print('Part 1: ',room.count_safe_tiles())

    room = MapRoom(first_row, 400000)
    room.make_map()
    print('Part 2: ', room.count_safe_tiles())