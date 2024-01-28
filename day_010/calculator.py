from art import logo
import os

CLS = "cls"
CLEAR = "clear"
SYSTEM_WINDOWS = "nt"

YES = "y"
NO = "n"
EXIT = "e"

MAIN = "__main__"

ADD = "+"
SUB = "-"
MUL = "*"
DIV = "/"

def clear() -> None:
    """
    Clears the console screen.
    """
    os.system(CLS if os.name == SYSTEM_WINDOWS else CLEAR)

def format_two_decimal_places(value: float) -> str:
    """
    Formats a float value with two decimal places.

    Args:
    value (float): The value to be formatted.

    Returns:
    str: The formatted string.
    """
    return "{:.2f}".format(value)

def add(number_1: float, number_2: float) -> float:
    """
    Adds two numbers.

    Args:
    number_1 (float): The first number.
    number_2 (float): The second number.

    Returns:
    float: The sum of the two numbers.
    """
    return number_1 + number_2

def sub(number_1: float, number_2: float) -> float:
    """
    Subtracts the second number from the first.

    Args:
    number_1 (float): The first number.
    number_2 (float): The second number.

    Returns:
    float: The result of the subtraction.
    """
    return number_1 - number_2

def mul(number_1: float, number_2: float) -> float:
    """
    Multiplies two numbers.

    Args:
    number_1 (float): The first number.
    number_2 (float): The second number.

    Returns:
    float: The product of the two numbers.
    """
    return number_1 * number_2

def div(number_1: float, number_2: float) -> float:
    """
    Divides the first number by the second.

    Args:
    number_1 (float): The numerator.
    number_2 (float): The denominator.

    Returns:
    float: The result of the division.
    """
    if number_2 == 0:
        return float('inf')
    return number_1 / number_2

OPERATIONS = {
    ADD: add, 
    SUB: sub, 
    MUL: mul, 
    DIV: div,
}

def calculate(number_1: float, number_2: float, operation: str) -> float:
    """
    Calculates the result based on the selected operation.

    Args:
    number_1 (float): The first number.
    number_2 (float): The second number.
    operation (str): The operation to be performed.

    Returns:
    float: The result of the calculation.
    """
    if operation in OPERATIONS.keys():
        return OPERATIONS[operation](number_1, number_2)
    return None

def read_str(message: str) -> str:
    """
    Reads a string from the user.

    Args:
    message (str): The message to display.

    Returns:
    str: The input string.
    """
    return input(message)

def read_number(message: str) -> float:
    """
    Reads a number from the user.

    Args:
    message (str): The message to display.

    Returns:
    float: The input number.
    """
    return float(input(message)) 

def read_operation() -> str:
    """
    Reads and validates the selected operation from the user.

    Returns:
    str: The selected operation.
    """
    operation = ''
    while operation not in OPERATIONS:
        operation = read_str("\nPick an operation: ")
    return operation

def show_operations() -> None:
    """
    Displays the available operations.
    """
    [print(f"\n{op}") for op in OPERATIONS]

def show_result(number_1: float, number_2: float, operation: str, result: float) -> None:
    """
    Displays the calculation result.

    Args:
    number_1 (float): The first number.
    number_2 (float): The second number.
    operation (str): The operation performed.
    result (float): The result of the calculation.
    """
    print("\n\n{:.2f} {} {:.2f} = {:.2f}".format(number_1, operation, number_2, result))

def run_calculator() -> None:
    """
    Runs the calculator program.
    """
    while True:
        clear()
        print(f"\n{logo}\n")
        number_1 = read_number("\nWhat's the first number?: ")
        
        show_operations()

        continue_calculating = YES

        while continue_calculating == YES:
            operation = read_operation()

            number_2 = read_number("\nWhat's the next number?: ")

            result = calculate(number_1, number_2, operation)

            show_result(number_1, number_2, operation, result)
            
            number_1 = result
            continue_calculating = read_str("Type '{}' to continue calculating with {:.2f}, '{}' to start a new calculation, or type '{}' to exit the program.: ".format(YES, result, NO, EXIT))

            if continue_calculating == EXIT:
                return

if __name__ == MAIN:
    try:
        run_calculator()
    except (KeyboardInterrupt, ValueError):
        print("\nAn error has occurred, the program will be terminated!\n")
    finally: 
        clear()