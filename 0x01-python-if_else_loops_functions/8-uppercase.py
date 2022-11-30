#!/usr/bin/python3


def uppercase(string: str) -> None:
    """
    A function that convert a string to uppercase
    and then prints it.

    Args:
        str (str): the string to be converted to uppercase
    """
    str_list: list[str] = list(string)
    for index, char in enumerate(str_list):
        if ord(char) > 96 and ord(char) < 123:
            str_list[index] = chr(65 + ord(char) - 97)
    print("{}".format("".join(str_list)))
