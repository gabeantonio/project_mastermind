# Mastermind

PROCESS

1. I plan on creating two scripts for this project: One script that will handle the interface on the command line, and one script that will handle the game logic.
2. mastermind.py will contain the game logic while initialize_mastermind will take care of the terminal interface.
3. Starting with mastermind.py, I first want to initialize a hidden variable that will hold the random 4 number combination from the API.
4. Then, I want to also create a list that will hold the player's guesses as the game progresses.
5. I want to create a variable that will hold the allowed attempts at guessing as well as the word length. (10 attemps, 4 numbers - as stated in the prompt).
6. I then want to write a function that will handle the winning logic.
7. Then, I can write logic for what to do when a user attempts a guess the combination.
8. Now, I want to run the entriety of the game through a loop, so I will create a function that checks if the user still has remaining guesses. 