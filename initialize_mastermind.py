from mastermind import Mastermind

class Game:
    def main():
        mastermind = Mastermind('1234')
        while mastermind.continue_game:
            user_guess = input('Type your guess here: ')

    if __name__ == '__main__':
        main()
