from mastermind import Mastermind
import requests
from colorama import Fore
import time
import math

def main():
    combination = generate_combination()
    mastermind = Mastermind(combination)
    print(combination, '<------ COMBINATION')
    player_score = 0
    start = time.time()
    while mastermind.continue_game():
        user_guess = input('\nType your guess here: ')
        if not user_guess.isnumeric():
            print(Fore.RED + f'\nPlease enter numbers only. \n' + Fore.RESET)
            continue
        if len(user_guess) != len(combination):
            print(Fore.RED + f'\nInput is either too short or too long. Please make sure your input is {len(combination)} digits long. \n' + Fore.RESET)
            continue

        mastermind.add_guess(user_guess)
        guesses = mastermind.user_guesses()
        check = mastermind.check(user_guess)

        if all_incorrect(check):
            print(Fore.RED + f'Sorry, all are incorrect. \n' + Fore.RESET)
        else:
            feedback(guesses, check)

    # Add logic that will check to see if the most recent guess is correct or not:
    if mastermind.correct_guess:
        end = time.time()
        duration = end - start
        player_score += math.floor((900 - duration) * 5)
        if player_score < 0:
            player_score = 0
        print(Fore.GREEN + f'You won! Your final score: {player_score} \n' + Fore.RESET)
    else:
        print(Fore.RED + f'You lost! Your final score: {player_score} \n' + Fore.RESET )

def generate_combination():
    api_url = f"https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new"
    response = requests.get(api_url)
    if response.status_code == 200:
        combination = f'{response.text}'.replace('\n', '')
        return combination
    else:
        print(f'Failed to get a random combination. Status code: {response.status_code}')

def all_incorrect(check):
    if check[0] == 0:
        return True
    
def feedback(guesses, check):
    print(Fore.GREEN + f'You guessed {check[0]} correct numbers in {check[1]} correct positions. You have {10 - len(guesses)} attempts remaining. Your previous guesses: {guesses} \n' + Fore.RESET)  


if __name__ == '__main__':
    main()
