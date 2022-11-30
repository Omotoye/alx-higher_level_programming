#!/usr/bin/python3


def islower(c: str) -> bool:
    """This function check if a character is
    lowercase

    Args:
        c (str): the character to be checked

    Returns:
        bool: True if lowercase, False otherwise
    """
    if ord(c) > 96 and ord(c) < 123:
        return True
    else:
        return False
