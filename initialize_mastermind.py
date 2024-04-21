from mastermind import Mastermind


def main():
    mastermind = Mastermind('1234')
    while mastermind.continue_game:
        user_guess = input('Type your guess here: ')
        mastermind.add_guess(user_guess)
        guesses = mastermind.user_guesses()
        print('GUESSES --->', guesses)
        # Add logic that will check to see if the most recent guess is correct or not:
        if check(user_guess,  mastermind.combination):
            print('You won!')
            break
        else:
            print('Try again!')
    

def check(user_guess, combination):
    if user_guess == combination:
        return True
    else:
        return False
    
if __name__ == '__main__':
    main()
