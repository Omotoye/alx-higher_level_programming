#!/usr/bin/python3


def search_replace(my_list, search: int, replace: int):
    """A function that replaces all occurrences of an element
    by another in a new list

    Args:
        my_list (list[int]): The initial list
        search (int): The element to replace in the list
        replace (int): The new element

    Returns:
        list[int]: The new list with the specified element replaced
    """
    return list(map(lambda x: replace if x == search else x, my_list))
