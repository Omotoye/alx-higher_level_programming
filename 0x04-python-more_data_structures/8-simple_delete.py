#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    """A function that deletes a key in a dictionary

    Args:
        a_dictionary (dict[str, Any]): the dictionary to delete from
        key (str, optional): the key to delete. Defaults to "".

    Returns:
        dict[str, Any]: the new dictionary after key deletion
    """
    if key in a_dictionary.keys():
        a_dictionary.pop(key)
    return a_dictionary
