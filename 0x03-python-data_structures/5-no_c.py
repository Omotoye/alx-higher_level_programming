#!/usr/bin/python3


def no_c(my_string: str) -> str:
    """A function that removes all characters `c` and `C` from
    a string

    Args:
        my_string (str): the string to remove char `c` and `C` from

    Returns:
        str: the new string after the char removal operation
    """
    my_string_char_list = list(my_string)
    for index, char in enumerate(my_string_char_list):
        if char == "c" or char == "C":
            my_string_char_list[index] = ""
    return "".join(my_string_char_list)
