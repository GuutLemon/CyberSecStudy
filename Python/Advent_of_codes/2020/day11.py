with open('day11.txt') as f:
    read_data = f.read().strip().split('\n')


class Plane():
    def __init__(self, seats):
        self.seats = seats
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

    def main(self):
        print(self.seat_change())

    def seat_change(self):
        while True:
            loop_check = 0
            new_seats = self.seats[::]
            for row in range(len(self.seats)):
                for col in range(len(self.seats[0])):
                    adjacents = self.find_adjacents2(row, col)  # Part 2

                    if new_seats[row][col] == 'L' and all(a != '#' for a in adjacents):
                        new_seats[row] = new_seats[row][:col] + '#' + new_seats[row][col+1:]
                        loop_check = 1
                    elif new_seats[row][col] == '#' and adjacents.count('#') >= 5:  # Part 2
                        new_seats[row] = new_seats[row][:col] + 'L' + new_seats[row][col+1:]
                        loop_check = 1

            if loop_check == 0:
                return self.result()
            self.seats = new_seats[::]

    def result(self):
        count = 0
        for row in range(len(self.seats)):
            for col in range(len(self.seats[0])):
                if self.seats[row][col] == '#':
                    count += 1
        return count

    def find_adjacents(self, row, col):
        adjacents = []
        for r, c in self.directions:
            nrow = row + r
            ncol = col + c
            if 0 <= nrow < len(self.seats) and 0 <= ncol < len(self.seats[0]):
                adjacents.append(self.seats[nrow][ncol])
        return adjacents

    # Part 2
    def find_adjacents2(self, row, col):
        adjacents = []
        for r, c in self.directions:
            nrow = row
            ncol = col
            for _ in self.seats:
                nrow += r
                ncol += c
                if 0 <= nrow < len(self.seats) and 0 <= ncol < len(self.seats[0]):
                    if self.seats[nrow][ncol] != '.':
                        adjacents.append(self.seats[nrow][ncol])
                        break
                else:
                    break
        return adjacents


p = Plane(read_data)
p.main()