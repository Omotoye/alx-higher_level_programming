#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """A function that replaces an element in a list

    Args:
        my_list (list[int]): the list to be operated on
        idx (int): the index of element to be replaced
        element (int): the element to put in the list

    Returns:
        list[int]: the new list created
    """
    if idx in range(0, len(my_list)):
        my_list[idx] = element
    return my_list
