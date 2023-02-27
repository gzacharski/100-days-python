# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random


def check_the_answer(the_number, guess):
    if the_number == guess:
        return True
    elif guess < the_number:
        print("Too low")
        print("Guess again")
        return False
    else:
        print("Too high")
        print("Guess again")
        return False


def check_the_guess_number(the_number, the_number_of_attempts):
    for i in range(the_number_of_attempts):
        print(f"You have {the_number_of_attempts - i} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if check_the_answer(the_number, guess):
            return True
    return False


def set_difficulty():
    level_dictionary = {
        'easy': 10,
        'hard': 5
    }
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    return level_dictionary[difficulty]


def choose_random_int():
    print("I'm thinking of the number between 1 and 100.")
    return random.randint(1, 100)


print("Welcome to the Number Guessing Game!")
number = choose_random_int()
number_of_attempts = set_difficulty()

if check_the_guess_number(number, number_of_attempts):
    print(f"You got it! The answer was {number}")
else:
    print("Ops, You lose")
