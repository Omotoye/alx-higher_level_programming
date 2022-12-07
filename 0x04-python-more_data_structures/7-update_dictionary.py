#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    """A function that replaces or adds key/value in a dictionary

    Args:
        a_dictionary (dict[str, Any]): the initial dictionary
        key (str): the key for the value to be changed or added
        value (Any): the new value for the given key

    Returns:
        dict[str, Any]: the new dictionary after updating/adding the
            the new key/value pair
    """
    a_dictionary.update({key: value})
    return a_dictionary
