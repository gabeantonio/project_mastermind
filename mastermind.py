import requests
import time
import math
import random
from colorama import Fore

class Mastermind:

    TOTAL_TRIES = 10
    EASY_MODE = 4
    HARD_MODE = 5
    MAX_TIME = 900
    MESSAGES = {
        "instructions": "Welcome to Mastermind! Try to guess the secret code consisting of {} numbers between 0 and 7. You have 10 attempts to guess correctly. Good luck! ",
        "numbers_only": "Please only enter numbers.",
        "wrong_length": "Input is either too short or too long. Please make sure your input is {} digits long.",
        "difficulty": "Please input either Easy or Hard.",
        "entirely_incorrect": "Sorry, all the numbers are incorrect.",
        "hint_error": "Please input either yes or no.",
        "hint_needed": "One of the numbers is {}",
        "no_hint": "Okay, good luck!",
        "win": "You won! Your final score: {}",
        "lose": "You failed to guess the combination! Your final score: {}"
    }

    def __init__(self):
        self.combination = self.generate_combination(self.difficulty())
        self.guesses = []

    def generate_combination(self, difficulty_level):
        api_url = f"https://www.random.org/integers/?num={difficulty_level}&min=0&max=7&col=1&base=10&format=plain&rnd=new"
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            combination = f'{response.text}'.replace('\n', '')
            return combination
        except requests.RequestException as error:
            print(f'Failed to get a combination from API: {error}. Generating random number instead.')
            return ''.join(str(random.randint(0, 7)) for _ in range(difficulty_level))

    def check(self, guess: str):
        in_combination, in_position = [], 0
        for i in range(len(self.combination)):
            number = guess[i]
            if number in self.combination:
                in_combination.append(number)
            if number == self.combination[i]:
                in_position += 1
        correct_numbers = len(set(in_combination))
        return [correct_numbers, in_position]

    @property
    def correct_guess(self):
        return len(self.guesses) > 0 and self.guesses[-1] == self.combination

    def continue_game(self):
        return self.TOTAL_TRIES - len(self.guesses) > 0 and not self.correct_guess
        
    def add_guess(self, guess: str):
        self.guesses.append(guess)
    
    def get_user_guess(self):
        while True:
            user_guess = input('\nType your guess here: ')
            if not user_guess.isnumeric():
                print(Fore.RED + f'\n{self.MESSAGES["numbers_only"]}\n' + Fore.RESET) 
            elif len(user_guess) != len(self.combination):
                print(Fore.RED + f'\n{self.MESSAGES["wrong_length"].format(len(self.combination))}\n' + Fore.RESET)
            else:
                return user_guess

    def display_feedback(self, feedback):
        return Fore.GREEN + f'You guessed {feedback[0]} correct numbers in {feedback[1]} correct positions. ' \
                            f'You have {self.TOTAL_TRIES - len(self.guesses)} attempts remaining. ' \
                            f'Your previous guesses: \n {self.guesses}\n' + Fore.RESET  
    
    def all_incorrect(self, feedback):
        return feedback[0] == 0
    
    def difficulty(self):
        while True:
            desired_difficulty = input('\nDo you want to play on Easy or Hard mode? ')
            if desired_difficulty != 'Easy' and desired_difficulty != 'Hard':
                print(Fore.RED + f'\n{self.MESSAGES["difficulty"]}\n' + Fore.RESET) 
            else:
                break
        if desired_difficulty == "Easy":
            return self.EASY_MODE
        if desired_difficulty == "Hard":
            return self.HARD_MODE

    def hint(self):
        while True:
            hint_needed = input("Do you need a hint? ")
            if hint_needed != 'yes' and hint_needed != 'no':
                print(Fore.RED + f'\n{self.MESSAGES["hint_error"]}\n' + Fore.RESET) 
            else:
                break
        if hint_needed == "yes":
            random_index = random.randint(0, len(self.combination) - 1)
            return Fore.CYAN + f'\n{self.MESSAGES["hint_needed"].format(self.combination[random_index])}\n' + Fore.RESET
        if hint_needed == "no":
            return Fore.CYAN + f'\n{self.MESSAGES["no_hint"]}\n' + Fore.RESET

    def display_instructions(self):
        return Fore.GREEN + f'\n{self.MESSAGES["instructions"].format(len(self.combination))}\n' + Fore.RESET
    
    def play(self):
        print(self.display_instructions())
        print(self.combination, '<------ COMBINATION')
        player_score = 0
        start = time.time()
        while self.continue_game():
            user_guess = self.get_user_guess()
            self.add_guess(user_guess)
            feedback = self.check(user_guess)
            if self.all_incorrect(feedback):
                print(Fore.RED + f'{self.MESSAGES["entirely_incorrect"]}\n' + Fore.RESET)
                print(self.hint())
            else:
                print(self.display_feedback(feedback))
        if self.correct_guess:
            end = time.time()
            duration = end - start
            player_score += math.floor((self.MAX_TIME - duration) * 5)
            if player_score < 0:
                player_score = 0
            print(Fore.GREEN + f'{self.MESSAGES["win"].format(player_score)}\n' + Fore.RESET) 
        else:
            print(Fore.RED + f'{self.MESSAGES["lose"].format(player_score)}\n' + Fore.RESET ) 

if __name__ == "__main__":
    game = Mastermind()
    game.play()