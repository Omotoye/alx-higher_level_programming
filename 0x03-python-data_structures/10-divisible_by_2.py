#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """A function that finds all multiples of 2 in a list, it returns
    a new list True of False, depending on whether the integer at the
    same position in the original list is a multiple of 2

    Args:
        my_list (list[int], optional): the given list to check the items
            if they are multiples of 2. Defaults to [].

    Returns:
        list[bool]: a list of bool that mirrors the given list depending
            whether or not each item is a multiple of 2
    """
    new_list = []
    for num in my_list:
        new_list.append(True if num % 2 == 0 else False)
    return new_list
