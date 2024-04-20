class Mastermind:

    TOTAL_TRIES = 10
    COMBINATION_LENGTH = 4

    def __init__(self, combination: str):
        self.combination = combination
        self.guesses = []