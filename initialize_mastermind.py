from mastermind import Mastermind

class Game:
    def main():
        mastermind = Mastermind('')
        while mastermind.continue_game:
            user_guess = input('Type your guess here: ')
            mastermind.add_guess(user_guess)
            guesses = mastermind.user_guesses()
            print('GUESSES --->', guesses)

    if __name__ == '__main__':
        main()
