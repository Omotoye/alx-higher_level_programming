#!/usr/bin/python3


def remove_char_at(string: str, n: int) -> str:
    """A function that creates a copy of the string,
    removing the character at the position n

    Args:
        string (str): the given string to remove character
            from
        n (int): the index of the character to be removed

    Returns:
        str: the new string with the removed character
    """
    string_list: list[str] = list(string)
    if n < len(string_list) and n >= 0:
        del string_list[n]
    return "".join(string_list)
