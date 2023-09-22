with open('day25.txt') as f:
    read_data = f.read().strip().split('\n')
    init_state = [list(_) for _ in read_data]


class HerdMovement:
    def __init__(self, grid):
        self.grid = grid[::]
        # self.e_facing = []
        # self.s_facing = []
        self.dot = []
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                # if self.grid[r][c] == '>':
                #     self.e_facing.append((c, r))
                # elif self.grid[r][c] == 'v':
                #     self.s_facing.append((c, r))
                if self.grid[r][c] == '.':
                    self.dot.append((c, r))

    def main(self):
        turn = 0
        while True:
        # for i in range(1):
            turn += 1
            moving = self.dot_left_moving() + self.dot_up_moving()      # Don't use if-or
            if moving == 0:
                break
            # self.print_gird()
        print(turn)

    # Use 1 list instead of 2
    # Use 1 thing to check 2
    def dot_left_moving(self):
        movable = []
        for i in range(len(self.dot)):
            dc, dr = self.dot[i]
            left = (dc - 1) % len(self.grid[0])
            if self.grid[dr][left] == '>':
                movable.append(i)
        if movable:
            for m in movable:
                dc, dr = self.dot[m]
                left = (dc - 1) % len(self.grid[0])
                self.grid[dr][left] = '.'
                self.grid[dr][dc] = '>'
                self.dot[m] = (left, dr)
        return movable != []

    def dot_up_moving(self):
        movable = []
        for i in range(len(self.dot)):
            dc, dr = self.dot[i]
            up = (dr - 1) % len(self.grid)
            if self.grid[up][dc] == 'v':
                movable.append(i)
        if movable:
            for m in movable:
                dc, dr = self.dot[m]
                up = (dr - 1) % len(self.grid)
                self.grid[up][dc] = '.'
                self.grid[dr][dc] = 'v'
                self.dot[m] = (dc, up)
        return movable != []


    # Too slow
    # def e_moving(self):
    #     movable = []
    #     for c in range(len(self.e_facing)):
    #         ec, er = self.e_facing[c]
    #         neighbour = ((ec + 1) % len(self.grid[0]), er)
    #         if neighbour not in self.e_facing and neighbour not in self.s_facing:     # The slow part
    #             movable.append(c)
    #     for m in movable:
    #         ec, er = self.e_facing[m]
    #         self.e_facing[m] = ((ec + 1) % len(self.grid[0]), er)
    #     return movable != []
    #
    # def s_moving(self):
    #     movable = []
    #     for c in range(len(self.s_facing)):
    #         sc, sr = self.s_facing[c]
    #         neighbour = (sc, (sr + 1) % len(self.grid))
    #         if neighbour not in self.e_facing and neighbour not in self.s_facing:
    #             movable.append(c)
    #     for m in movable:
    #         sc, sr = self.s_facing[m]
    #         self.s_facing[m] = (sc, (sr + 1) % len(self.grid))
    #     return movable != []

    def print_gird(self):
        # result = [['.' for c in range(len(self.grid[0]))] for r in range(len(self.grid))]
        # for e in self.e_facing:
        #     result[e[1]][e[0]] = '>'
        # for s in self.s_facing:
        #     result[s[1]][s[0]] = 'V'
        for i in self.grid:
            print(''.join(i))
        print()


if __name__ == '__main__':
    cucumber = HerdMovement(init_state)
    cucumber.main()
