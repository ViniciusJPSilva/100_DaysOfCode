import os
from random import randint

CLS = "cls"
CLEAR = "clear"
SYSTEM_WINDOWS = "nt"

EASY = "Easy"
HARD = "Hard"

CODE = "Code"
ATTEMPTS = "Attempts"

GAME_OVER = 0

TOO_HIGH = 1
HIT = 0
TOO_LOW = -1

MIN_NUMBER = 1
MAX_NUMBER = 100

MODES = {
    EASY: {
        CODE: 1, 
        ATTEMPTS: 10,
    },
    HARD: {
        CODE: 2, 
        ATTEMPTS: 5,
    },
}

MAIN = "__main__"

def clear() -> None:
    """
    Clears the console screen.
    """
    os.system(CLS if os.name == SYSTEM_WINDOWS else CLEAR)

def read_number(message: str = "") -> int:
    """
    Reads an integer from the user, handling potential ValueError.
    
    :param message: The prompt message.
    :return: The entered integer.
    """
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print("\nInvalid value! Try again.")

def get_attempts_by_difficulty_code(code: int) -> int:
    """
    Gets the number of attempts for a given difficulty code.
    
    :param code: The difficulty code.
    :return: The number of attempts.
    """
    for difficulty_key in MODES:
        if MODES[difficulty_key][CODE] == code:
            return MODES[difficulty_key][ATTEMPTS]
    return None

def read_difficulty() -> int:
    """
    Reads the difficulty level from the user and returns the corresponding number of attempts.
    
    :return: The number of attempts for the chosen difficulty.
    """
    attempts = None
    while not attempts:
        attempts = get_attempts_by_difficulty_code(read_number(f"\n{MODES[EASY][CODE]} - Easy\n{MODES[HARD][CODE]} - Hard\nChoose a difficulty: "))
    return attempts

def check_guess(guess: int, number: int) -> int:
    """
    Compares the user's guess with the secret number and returns the result code.
    
    :param guess: The user's guess.
    :param number: The secret number.
    :return: Result code (HIT, TOO_HIGH, TOO_LOW).
    """
    return HIT if guess == number else TOO_HIGH if guess > number else TOO_LOW

def get_results(attempts: int, secret_number: int) -> str:
    """
    Generates the final game result message based on the number of attempts and the secret number.
    
    :param attempts: The remaining attempts.
    :param secret_number: The secret number.
    :return: The result message.
    """
    return f"\nYou got it! The answer was {secret_number}.\n" if attempts > GAME_OVER else f"\nYou've run out of guesses, you lose! The answer was {secret_number}.\n"

def guess_the_number() -> None:
    """
    Main function to run the Number Guessing Game.
    """
    while True:
        clear()
        print(f"Welcome to the Number Guessing Game!\nI'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}.")

        attempts = read_difficulty()
        secret_number = randint(MIN_NUMBER, MAX_NUMBER)

        while attempts > GAME_OVER:
            result = check_guess(read_number(f"\nYou have {attempts} attempts remaining to guess the number.\nMake a guess: "), secret_number)

            if result == HIT:
                break

            print("\nToo low." if result == TOO_LOW else "\nToo high.")
            attempts -= 1

        print(get_results(attempts, secret_number))
        input("Press <ENTER> to continue")

if __name__ == MAIN:
    try:
        guess_the_number()
    except (KeyboardInterrupt, ValueError):
        print("\nAn error has occurred, the program will be terminated!\n")
    finally: 
        clear()
