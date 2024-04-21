from mastermind import Mastermind
import requests

def main():
    combination = generate_combination()
    mastermind = Mastermind(combination)
    print(combination, '<------ COMBINATION')
    while mastermind.continue_game():
        user_guess = input('Type your guess here: ')
        mastermind.add_guess(user_guess)
        guesses = mastermind.user_guesses()
        check = mastermind.check(user_guess)
        feedback(guesses, check)

        

    # Add logic that will check to see if the most recent guess is correct or not:
    if mastermind.correct_guess:
        print('You won!')
    else:
        print('You lost!')

def generate_combination():
    api_url = f"https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new"
    response = requests.get(api_url)
    if response.status_code == 200:
        combination = f'{response.text}'.replace('\n', '')
        return combination
    else:
        print(f'Failed to get a random combination. Status code: {response.status_code}')

def feedback(guesses, check):
    print(f'You guessed {check[0]} correct numbers in {check[1]} correct positions. You have {10 - len(guesses)} attempts remaining. Your previous guesses: {guesses} \n' )    

if __name__ == '__main__':
    main()
