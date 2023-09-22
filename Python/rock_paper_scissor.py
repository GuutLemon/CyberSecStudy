import random


class Game():
    def __init__(self):
        self.win_count = 0
        self.lost_count = 0
        self.tie_count = 0

    def run(self):
        self.print_welcome_massage()
        while True:
            user_move = self.user_move()
            if user_move == 'q':
                self.count_results()
                break
            comp_move = self.comp_move()
            self.evaluate_moves(user_move, comp_move)

    def print_welcome_massage(self):
        print("""
        Welcome to Rock-Paper-Scissor!
        (Press 'r' for rock, 'p' for paper, 's' for scissor and 'q' to quit)
        """)

    def user_move(self):
        inp = input("What's your move? ").lower()
        valid_choices = ['r', 'p', 's', 'q']
        if inp not in valid_choices:
            print("Invalid choice!")
            return self.user_move()
        return inp

    def comp_move(self):
        moves_lst = ['r', 'p', 's']
        return random.choice(moves_lst)

    def evaluate_moves(self, user, comp):
        move_dct = {'r': 'rock', 'p': 'paper', 's': 'scissor'}
        if (user == 'r' and comp == 's') or \
            (user == 'p' and comp == 'r') or \
                (user == 's' and comp == 'p'):
            print(f"I chose {move_dct[comp]}, you win!")
            self.win_count += 1
        elif user == comp:
            print(f"I chose {move_dct[comp]}, it's a tie!")
            self.tie_count += 1
        else:
            print(f"I chose {move_dct[comp]}, you lose!")
            self.lost_count += 1

    def count_results(self):
        total_matches = self.win_count + self.lost_count + self.tie_count
        print(f"""
    Total matches: {total_matches}
    Win counts: {self.win_count}
    Lost counts: {self.lost_count}
    Tie counts: {self.tie_count}
    """)


if __name__ == '__main__':
    game = Game()
    game.run()
