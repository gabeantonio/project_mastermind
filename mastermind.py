class Mastermind:

    TOTAL_TRIES = 10
    COMBINATION_LENGTH = 4

    def __init__(self, combination: str):
        self.combination = combination
        self.guesses = []

    # Write winning logic:
    def correct_guess(self):
        if self.guesses[-1] == self.combination:
            return True
        else:
            return False

    # Write logic in the event that a user attempts a combination:
    def add_guess(self, guess: str):
        self.guesses.append(guess)

    # Write logic that checks if a user can still make guesses:
    def continue_game(self):
        if self.TOTAL_TRIES - len(self.guesses) == 0 and not self.correct_guess:
            return True
        else:
            return False
        
    # Write logic that adds a user's guesses to the self.guesses array:
    def add_guess(self, guess: str):
        self.guesses.append(guess)
        
    # Write logic for a user to be able to view their past guesses:
    def user_guesses(self):
        return self.guesses
    

    