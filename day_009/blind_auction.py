from typing import Tuple
from art import logo
import os

CLS = "cls"
CLEAR = "clear"
SYSTEM_WINDOWS = "nt"

YES = "yes"
NO = "no"

MAIN = "__main__"


def clear() -> None:
    """
    Clears the console screen.
    """
    os.system(CLS if os.name == SYSTEM_WINDOWS else CLEAR)


def read_bidder_data() -> Tuple[str, float, bool]:
    """
    Reads bidder data including name, bid, and whether there are more bidders.

    Returns:
    Tuple[str, float, bool]: A tuple containing name, bid, and a boolean indicating if there are more bidders.
    """
    name = input("\nWhat is your name?\n")
    
    bid = 0
    while bid <= 0:
        bid = float(input("\nWhat's your bid?\n$"))
        if bid <= 0:
            print("\nWARNING: Bid must be greater than 0!")

    has_next = ""
    while has_next != YES and has_next != NO:
        has_next = input("\nAre there any other bidders? Type 'yes' or 'no'.\n")

    return (name, bid, True if has_next == YES else False)


def add_bidder(bidders: dict, name: str, bid: float) -> None:
    """
    Adds a bidder to the dictionary of bidders.

    Args:
    bidders (dict): The dictionary containing bidders.
    name (str): The name of the bidder.
    bid (float): The bid amount.
    """
    bidders[name] = bid


def get_winning_bidder(bidders: dict) -> Tuple[str, float]:
    """
    Gets the winning bidder from the dictionary of bidders.

    Args:
    bidders (dict): The dictionary containing bidders.

    Returns:
    Tuple[str, float]: A tuple containing the name and bid of the winning bidder.
    """
    dict(sorted(bidders.items(), key = lambda item: item[1]))
    winner_name = list(bidders.keys())[-1]

    return (winner_name, bidders[winner_name])

def format_two_decimal_places(value: float) -> str:
    """
    Formats a float value with two decimal places.

    Args:
    value (float): The value to be formatted.

    Returns:
    str: The formatted string.
    """
    return "{:.2f}".format(value)


def run_auction() -> None:
    """
    Runs the auction program, collecting bids and determining the winner.
    """
    bidders = {}
    has_next = True 

    while has_next:
        print(f"{logo}\n\nWelcome to the secret auction program.\n")
        name, bid, has_next = read_bidder_data()
        add_bidder(bidders, name, bid)
        clear()

    winner_name, winner_bid = get_winning_bidder(bidders)

    print(f"{logo}\n\nThe winner is {winner_name} with a bid of ${format_two_decimal_places(winner_bid)}!\n\n")


if __name__ == MAIN:
    try:
        clear()
        run_auction()
    except (KeyboardInterrupt, ValueError):
        print("\nAn error has occurred, the program will be terminated!\n")