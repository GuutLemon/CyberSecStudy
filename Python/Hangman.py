import random
import sys


class Hangman():
    def __init__(self, word_lst):
        self.secret = self.get_secret(word_lst)
        self.len_secret = len(self.secret)
        self.turns = self.len_secret
        self.displayed_secret = ["[]" for i in range(self.len_secret)]

    def run(self):
        self.print_welcome_message(self.len_secret)
        for turn in range(self.turns, 0, -1):
            user_guess = self.get_user_input()
            if user_guess == 'quit':
                sys.exit()
            self.evaluate_guess(user_guess)
            if self.win_check():
                sys.exit()
            print(f"You have {turn - 1} turns left.")
        if not self.final_guess():
            print(f"You've lost! The secret word is {self.secret}")

    def print_welcome_message(self, len_secret):
        print("""
        Welcome to Hangman!
        Please guess the secret word! (Enter 'quit' to quit)
        """)
        print("".join(self.displayed_secret))
        print(f"You have {self.len_secret} turns to guess the word.")

    def get_secret(self, word_lst):
        if len(word_lst) >= 1 and all(word.isalpha() for word in word_lst):
            return random.choice(word_lst)
        raise ValueError(
            "Invalid word list! Please make sure list is not empty nor contains empty word!")

    def get_user_input(self):
        guess = input("Guess a letter: ")
        if guess == 'quit':
            return guess
        elif len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please guess a letter!")
            return self.get_user_input()
        return guess

    def evaluate_guess(self, guess):
        count = 0
        pos = []
        for i, l in enumerate(self.secret):
            if guess == l:
                count += 1
                pos.append(i)
        if count > 0:
            print(f"The word has {count} letter(s) '{guess}' in it!")
            self.reveal_secret(guess, pos)
        else:
            print(f"The word has no letter {guess} in it!")
            self.reveal_secret(None, pos)

    def reveal_secret(self, guess, pos):
        if not guess:
            return
        for i in pos:
            self.displayed_secret[i] = guess
        print("".join(self.displayed_secret))

    def win_check(self):
        if "[]" not in self.displayed_secret:
            print("Congrat, you've guessed the word!")
            return 'w'

    def final_guess(self):
        final = input("Final chance! Can you type out the word? ")
        if final == self.secret:
            print("Congrat, you've guessed the word!")
            return 'w'


if __name__ == '__main__':
    word_lst = ['papyrus', 'mango', 'apple', 'python', 'program', 'batman']
    game = Hangman(word_lst)
    game.run()
