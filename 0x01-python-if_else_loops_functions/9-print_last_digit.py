#!/usr/bin/python3


def print_last_digit(number: int) -> int:
    """Prints the last digit of a number

    Args:
        number (int): Integer to check for last number

    Returns:
        int: The last digit of the number given
    """
    last_digit: int = abs(number) % 10
    print("{}".format(last_digit), end="")
    return last_digit
