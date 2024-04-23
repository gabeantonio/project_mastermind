import requests
from colorama import Fore
import time
import math
import random

class Mastermind:

    TOTAL_TRIES = 10
    EASY_MODE = 4
    HARD_MODE = 5
    MESSAGES = {
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

    # Write a method that fetches the random number combination from the API:
    def generate_combination(self, difficulty_level):
        api_url = f"https://www.random.org/integers/?num={difficulty_level}&min=0&max=7&col=1&base=10&format=plain&rnd=new"
        response = requests.get(api_url)
        if response.status_code == 200:
            combination = f'{response.text}'.replace('\n', '')
            return combination
        else:
            print(f'Failed to get a combination from API. Status code: {response.status_code}. Generating random number instead.')
            return ''.join(str(random.randint(0, 7)) for _ in range(4))

    # Write a method that checks if the guess is correct, partially correct, or incorrect:
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

    # Write a method that checks if the user has won or not:
    @property
    def correct_guess(self):
        return len(self.guesses) > 0 and self.guesses[-1] == self.combination
        
    # Write a method that checks if a user can still make guesses:
    def continue_game(self):
        return self.TOTAL_TRIES - len(self.guesses) > 0 and not self.correct_guess
        
    # Write a method that adds a user's guesses to the self.guesses array:
    def add_guess(self, guess: str):
        self.guesses.append(guess)
    
    # Write a method that takes the user's guess anc validates it:
    def get_user_guess(self):
        while True:
            user_guess = input('\nType your guess here: ')
            if not user_guess.isnumeric():
                print(Fore.RED + f'\n{self.MESSAGES["numbers_only"]}\n' + Fore.RESET) 
            elif len(user_guess) != len(self.combination):
                print(Fore.RED + f'\n{self.MESSAGES["wrong_length"].format(len(self.combination))}\n' + Fore.RESET)
            else:
                return user_guess

    # Write a method that displays to the user some feedback regarding their most recent guess:
    def display_feedback(self, feedback):
        return Fore.GREEN + f'You guessed {feedback[0]} correct numbers in {feedback[1]} correct positions. ' \
                            f'You have {self.TOTAL_TRIES - len(self.guesses)} attempts remaining. ' \
                            f'Your previous guesses: \n {self.guesses}\n' + Fore.RESET  
    
    # Write a method that checks if a user's guess is entirely incorrect:
    def all_incorrect(self, feedback):
        return feedback[0] == 0
    
    # Write a method that allows a user to set the difficulty of the game:
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

    # Write a method that gives a user a hint if they need it:
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

    # Write a method that allows the user to play the game:
    def play(self):
        print("\nWelcome to Mastermind!")
        print(f"Try to guess the secret code consisting of {len(self.combination)} numbers between 0 and 7.")
        print("You have 10 attempts to guess correctly. Good luck!\n")
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

    # Add logic that will check to see if the most recent guess is correct or not:
        if self.correct_guess:
            end = time.time()
            duration = end - start
            player_score += math.floor((900 - duration) * 5)
            if player_score < 0:
                player_score = 0
            print(Fore.GREEN + f'{self.MESSAGES["win"].format(player_score)}\n' + Fore.RESET) 
        else:
            print(Fore.RED + f'{self.MESSAGES["lose"].format(player_score)}\n' + Fore.RESET ) 

if __name__ == "__main__":
    game = Mastermind()
    game.play()