#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary) -> None:
    """A function that prints a dictionary by ordered keys.

    Args:
        a_dictionary (dict[str, Any]): the dictionary to be printed
    """
    sorted_list_of_keys = sorted([key for key in a_dictionary.keys()])
    for key in sorted_list_of_keys:
        print("{}: {}".format(key, a_dictionary[key]))
