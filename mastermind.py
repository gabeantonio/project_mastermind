import requests
from colorama import Fore
import time
import math

class Mastermind:

    TOTAL_TRIES = 10

    def __init__(self):
        self.combination = self.generate_combination()
        self.guesses = []

    # Write a method that fetches the random number combination from the API:
    def generate_combination(self):
        api_url = f"https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new"
        response = requests.get(api_url)
        if response.status_code == 200:
            combination = f'{response.text}'.replace('\n', '')
            return combination
        else:
            print(f'Failed to get a random combination. Status code: {response.status_code}')
            exit()

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
        if len(self.guesses) > 0 and self.guesses[-1] == self.combination:
            return True
        else:
            return False
        
    # Write a method that checks if a user can still make guesses:
    def continue_game(self):
        if self.TOTAL_TRIES - len(self.guesses) > 0 and self.correct_guess == False:
            return True
        else: 
            return False
        
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
                print(Fore.RED + f'\n{self.MESSAGES["wrong_length"].format(len(self.combination))}\n' + Fore.RESET)  # Used message constant
            else:
                return user_guess

    # Write a method that displays to the user some feedback regarding their most recent guess:
    def display_feedback(self, feedback):
        return Fore.GREEN + f'You guessed {feedback[0]} correct numbers in {feedback[1]} correct positions. ' \
                            f'You have {self.TOTAL_TRIES - len(self.guesses)} attempts remaining. ' \
                            f'Your previous guesses: {self.guesses}\n' + Fore.RESET  
    
    # Write a method that checks if a user's guess is entirely incorrect:
    def all_incorrect(self, feedback):
        return feedback[0] == 0

    # Write a method that allows the user to play the game:
    def play(self):
        print("Welcome to Mastermind!")
        print("Try to guess the secret code consisting of 4 numbers between 0 and 7.")
        print("You have 10 attempts to guess correctly. Good luck!\n")
        print(self.combination, '<------ COMBINATION')
        player_score = 0
        start = time.time()
        while self.continue_game():

            user_guess = self.get_user_guess()
            self.add_guess(user_guess)
            feedback = self.check(user_guess)
            if self.all_incorrect(feedback):
                print(Fore.RED + f'{self.MESSAGES["all_incorrect"]}\n' + Fore.RESET)
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

    MESSAGES = {
        "numbers_only": "Please only enter numbers.",
        "wrong_length": "Input is either too short or too long. Please make sure your input is {} digits long.",
        "all_incorrect": "Sorry, all the numbers are incorrect.",
        "win": "You won! Your final score: {}",
        "lose": "You failed to guess the combination! Your final score: {}"
    }

if __name__ == "__main__":
    game = Mastermind()
    game.play()