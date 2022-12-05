#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """A function that replaces an element in a list at a specific
    position without modifying the original list (like in C)

    Args:
        my_list (list[int]): the list to take a copy of and modify
        idx (int): the index of the item in the list to be changed
        element (int): the item to item to set the given index to

    Returns:
        list[int]: copy of the new list
    """
    list_copy = my_list.copy()
    if idx in range(0, len(my_list)):
        list_copy[idx] = element
    return list_copy
