#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """A function that returns a new dictionary with all values
    multiplied by 2

    Args:
        a_dictionary (dict[str, int]): the given dictionary

    Returns:
        dict[str, int]: the new dictionary after multiplying all the
            itmes of the given dictioary by 2
    """
    new_dictionary = {}
    for key, value in a_dictionary.items():
        new_dictionary.update({key: value * 2})
    return new_dictionary
