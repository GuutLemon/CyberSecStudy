import re


class Tictactoe():
    def __init__(self):
        self.grid = [["[ ]" for _ in range(3)] for _ in range(3)]
        self.turn = 1
        self.symbol = ''
        self.player = 1

    def run(self):
        self.print_hello_message()
        while True:
            print(f"Turn {self.turn}")
            player = self.player_move()
            placement = self.placement(*player)
            if placement == "Invalid":
                continue
            self.print_grid()
            if self.win():
                break
            self.turn += 1

    def print_hello_message(self):
        print("""
Welcome to Tic-tac-toe!
Enter coordinate (exp: '1 3') to play, 'q' to quit
""")
        self.print_grid()

    def player_move(self):
        if self.turn % 2 == 1:
            self.symbol = '[X]'
            self.player = 1
        else:
            self.symbol = '[O]'
            self.player = 2
        coord_inp = input(f"Player {self.player}, enter your placement: ")
        if not re.match("^[1-3] [1-3]$", coord_inp):
            print("Invalid placement!")
            return self.player_move()
        # To work with indexes
        coord = [int(i) - 1 for i in coord_inp.split()]
        return coord, self.symbol

    def placement(self, coordinate, symbol):
        # Check already placed cell
        placement = self.grid[coordinate[0]][coordinate[1]]
        if placement != "[ ]":
            print("Invalid placement!")
            return "Invalid"
        self.grid[coordinate[0]][coordinate[1]] = symbol

    def print_grid(self):
        for i in self.grid:
            print("\t", end='')
            for j in i:
                print(j, end='')
            print()

    def win(self):
        for i in range(3):
            # Check rows
            if all(cell == self.symbol for cell in self.grid[i]):
                print(f"Player {self.player} has won!")
                return "w"
            # Check columns
            if all(row[i] == self.symbol for row in self.grid):
                print(f"Player {self.player} has won!")
                return "w"
        # Check negative diagonal
        if all(self.grid[i][2 - i] == self.symbol for i in range(3)):
            print(f"Player {self.player} has won!")
            return "w"
        # Check positive diagonal
        if all(self.grid[i][i] == self.symbol for i in range(3)):
            print(f"Player {self.player} has won!")
            return "w"
        # Check tie
        count = 0
        for i in range(3):
            if all("[ ]" not in cell for cell in self.grid[i]):
                count += 1
            else:
                count = 0
        if count == 3:
            print("It's a tie!")
            return 't'


game = Tictactoe()
game.run()
