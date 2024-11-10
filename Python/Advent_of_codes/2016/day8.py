class Screen:
    def __init__(self, instructions):
        self.instr = instructions
        self.grid = [['.']*50 for _ in range(6)]

    def print_scr(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                print(self.grid[i][j], end=' ')
            print('')

    def count_lit(self):
        count = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == '#':
                    count += 1
        return count

    def rect(self, size):
        size = size.split('x')
        x = int(size[0])
        y = int(size[-1])
        for i in range(y):
            for j in range(x):
                if self.grid[i][j] == '.':
                    self.grid[i][j] = '#'

    def copy_row(self, y):
        line = []
        for j in range(len(self.grid[0])):
            line.append(self.grid[y][j])
        return line

    def copy_col(self, x):
        line = []
        for i in range(len(self.grid)):
            line.append(self.grid[i][x])
        return line

    def shift_line(self, line, amount):
        return line[-amount:] + line[:-amount]

    def rot(self, instr):
        dir = instr[1]
        amount = int(instr[-1])
        if dir == 'row':
            y = int(instr[2][2:])
            row = self.copy_row(y)
            shifted_row = self.shift_line(row, amount)
            self.grid[y] = shifted_row.copy()
        elif dir == 'column':
            x = int(instr[2][2:])
            col = self.copy_col(x)
            shifted_col = self.shift_line(col, amount)
            for i in range(len(self.grid)):
                self.grid[i][x] = shifted_col[i]


if __name__ == '__main__':
    with open('day8.txt') as f:
        instructions = f.read().strip().replace('by ', '').split('\n')
        instructions = [_.split() for _ in instructions]

    scr = Screen(instructions)
    for instr in instructions:
        if instr[0] == 'rect':
            scr.rect(instr[-1])
        else:
            scr.rot(instr)
    scr.print_scr()
    print(scr.count_lit())

