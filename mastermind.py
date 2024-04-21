class Mastermind:

    TOTAL_TRIES = 10

    def __init__(self, combination: str):
        self.combination = combination
        self.guesses = []

    # Write winning logic:
    def correct_guess(self):
        if len(self.guesses) > 0 and self.guesses[-1] == self.combination:
            return True
        else:
            return False

    # Write logic in the event that a user attempts a combination:
    def add_guess(self, guess: str):
        self.guesses.append(guess)

    # Write logic that checks if a user can still make guesses:
    def continue_game(self):
        if self.TOTAL_TRIES - len(self.guesses) > 0 and not self.correct_guess:
            return True
        else:
            return False
        
    # Write logic that adds a user's guesses to the self.guesses array:
    def add_guess(self, guess: str):
        self.guesses.append(guess)

    # Write logic for a user to be able to view their past guesses:
    def user_guesses(self):
        return self.guesses
    
    # Write logic that checks if the guess is correct, partially correct, or incorrect:
    def check(self, guess: str):
        in_combination, in_position = [], 0
        for i in range(len(self.combination)):
            number = guess[i]
            if number in self.combination:
                in_combination.append(number)
            if number == self.combination[i]:
                in_position += 1
        correct_numbers = len(set(in_combination))
        return [correct_numbers, in_position, len(in_combination)]

    

    