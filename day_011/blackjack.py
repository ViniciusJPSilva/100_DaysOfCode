############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from typing import Callable
from art import logo
import os

CLS = "cls"
CLEAR = "clear"
SYSTEM_WINDOWS = "nt"

YES = "y"
NO = "n"
EXIT = "e"

BLACKJACK = 21

COMPUTER_LIMIT = 18

INITIAL_CARDS_QUANTITY = 2
HIT_CARDS_QUANTITY = 1

STATUS_BLACKJACK = 1
STATUS_DEFAULT = 0
STATUS_WENT_OVER = -1

ELEVEN = 11
ACE = 1

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

MAIN = "__main__"


def read_str(message: str) -> str:
    """
    Reads a string from the user.

    Args:
    message (str): The message to display.

    Returns:
    str: The input string.
    """
    return input(message)


def read_play() -> bool:
    """
    Reads the user's choice to continue playing.

    Returns:
    bool: True if the user wants another card, False if they want to pass.
    """
    option = read_str(f"\nType '{YES}' to get another card, type '{NO}' to pass: ")

    return True if option == YES else False


class Player:
    def __init__(self) -> None:
        """
        Initializes a new Player object with an empty list of cards.
        """
        self.cards = []

    def add_card(self, card: int) -> int:
        """
        Adds a card to the player's hand.

        Args:
        card (int): The card value to be added.

        Returns:
        int: The updated score of the player's hand.
        """
        if card in CARDS:
            self.cards.append(card)
            return self.get_score()
        return None
    
    def get_score(self) -> int:
        """
        Calculates and returns the current score of the player's hand.

        Returns:
        int: The player's current score.
        """
        score = sum(self.cards)
        if score > BLACKJACK and ELEVEN in self.cards:
            self.cards[self.cards.index(ELEVEN)] = ACE
            score = sum(self.cards)
        return score

    def check_blackjack(self) -> bool:
        """
        Checks if the player has a blackjack (score of 21).

        Returns:
        bool: True if the player has a blackjack, False otherwise.
        """
        return True if self.get_score() == BLACKJACK else False
    
    def remove_cards(self) -> 'Player':
        """
        Removes all cards from the player's hand.

        Returns:
        Player: The Player object with an empty hand.
        """
        self.cards = []
        return self

    
class Game:
    def __init__(self, reader: Callable) -> None:
        """
        Initializes a new Game object.

        Args:
        reader (Callable): A callable object used to get user input, must return a boolean.
        """
        self.player = Player()
        self.computer = Player()
        self.reader = reader
        self.started = False
    
    @staticmethod
    def draw_card() -> int:
        """
        Draws a card randomly from the available cards.

        Returns:
        int: The value of the drawn card.
        """
        return random.choice(CARDS)
    
    def start(self) -> str:
        """
        Starts a new round of the game by dealing initial cards to the player and computer.

        Returns:
        str: A message indicating the start of the game.
        """
        self.deal_cards(self.player.remove_cards(), INITIAL_CARDS_QUANTITY)
        self.deal_cards(self.computer.remove_cards(), INITIAL_CARDS_QUANTITY)
        self.started = True

    def next_round(self) -> str:
        """
        Executes the next round of the game.

        Returns:
        str: A message indicating the status of the round.
        """
        if not self.started: 
            return None
        
        # Checking if there was blackjack or the value has been exceeded
        if self.check_if_finished():
            return self.over()
        
        # Reading player hit
        if self.reader():
            self.deal_cards(self.player)
            return self.get_game_report()
        else: 
            return self.over()
        
    def check_if_finished(self) -> bool:
        """
        Checks if the game round has finished.

        Returns:
        bool: True if the game round has finished, False otherwise.
        """
        player_status = self.check_player_status(self.player)
        cpu_status = self.check_player_status(self.computer)

        return True if player_status == STATUS_BLACKJACK or player_status == STATUS_WENT_OVER or cpu_status == STATUS_WENT_OVER else False
            

    def over(self) -> str:
        """
        Ends the current round of the game and determines the winner.

        Returns:
        str: A message indicating the end of the round and the winner.
        """
        if self.check_player_status(self.player) != STATUS_WENT_OVER:
            self.computer_turn()

        message = f"\nYour final hand: {self.player.cards}, final score: {self.player.get_score()}"
        message += f"\nComputer's final hand: {self.computer.cards}, final score: {self.computer.get_score()}\n\n"
        message += self.get_final_message()
        message += "\n\n"

        self.started = False

        return message
    
    def computer_turn(self) -> None:
        """
        Executes the computer's turn in the current round.
        """
        player_score = self.player.get_score()
        computer = self.computer
        while computer.get_score() < player_score and computer.get_score() <= COMPUTER_LIMIT:
            self.deal_cards(computer)

    def check_player_status(self, player: Player) -> int:
        """
        Checks the status of a player (blackjack, went over, default).

        Args:
        player (Player): The player to check.

        Returns:
        int: The status of the player.
        """
        return STATUS_BLACKJACK if player.check_blackjack() else STATUS_WENT_OVER if player.get_score() > BLACKJACK else STATUS_DEFAULT

    def deal_cards(self, player: Player, quantity: int = 1) -> None:
        """
        Deals a specified quantity of cards to a player.

        Args:
        player (Player): The player to receive the cards.
        quantity (int): The number of cards to deal. Defaults to 1.
        """        
        for index in range(0, quantity):
            player.add_card(Game.draw_card())
    
    def get_computer_first_card(self) -> int:
        """
        Gets the value of the computer's first card.

        Returns:
        int: The value of the computer's first card.
        """        
        return self.computer.cards[0]
    
    def is_started(self) -> bool:
        """
        Checks if the game round has started.

        Returns:
        bool: True if the game round has started, False otherwise.
        """        
        return self.started 
    
    def get_game_report(self) -> str:
        """
        Generates a report of the current game status.

        Returns:
        str: A message with the player's current cards and score, and the computer's first card.
        """        
        return f"\nYour cards: {self.player.cards}, current score: {self.player.get_score()}\nComputer's first card: {self.get_computer_first_card()}"
    
    def get_final_message(self) -> str:
        """
        Generates a message indicating the final outcome of the game round.

        Returns:
        str: A message indicating the final outcome of the game round.
        """
        player_score = self.player.get_score()
        player_status = self.check_player_status(self.player)
        computer_score = self.computer.get_score()
        computer_status = self.check_player_status(self.computer)

        if player_score > computer_score and player_status != STATUS_WENT_OVER or player_score <= BLACKJACK and computer_status == STATUS_WENT_OVER:
            if player_status == STATUS_BLACKJACK:
                return "BLACKJACK! You win! 😎"
            else:
                return "CONGRATS! You win! 😁" 
        elif player_score == computer_score:
            if player_status == STATUS_BLACKJACK:
                return "IT'S A TIE! And both have BLACKJACK! 🫡"
            else:
                return "IT'S A TIE! Both had the same score! 🙂"
        else:
            if player_status == STATUS_WENT_OVER:
                return "YOU WENT OVER! And lose 🙁"
            else:
                return "COMPUTER WON! And you lose 🙁"
    
    
def clear() -> None:
    """
    Clears the console screen.
    """
    os.system(CLS if os.name == SYSTEM_WINDOWS else CLEAR)


def show_logo() -> None:
    """
    Clears the console and displays the game logo.
    """
    clear()
    print(logo)


def blackjack() -> None:
    """
    Main function to run the Blackjack game.
    """
    game = Game(read_play)

    while True:
        clear()
        show_logo()
        game.start()

        print(game.get_game_report())

        while game.is_started():
            print(game.next_round())

        if read_str(f"Do you want to play a new game? Type '{YES}' or '{NO}': ") == NO:
            break


if __name__ == MAIN:
    try:
        blackjack()
    except (KeyboardInterrupt, ValueError):
        print("\nAn error has occurred, the program will be terminated!\n")
    finally: 
        clear()