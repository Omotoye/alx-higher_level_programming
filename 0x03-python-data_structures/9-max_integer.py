#!/usr/bin/python3


def max_integer(my_list=[]):
    """A function that finds the biggest integer of a list

    Args:
        my_list (list[Optional[int]], optional): the list from which
            to check for the biggest integer. Defaults to [].

    Returns:
        Optional[int]: the max number if the list is not empty, None
            if the list is empty
    """
    max_num = my_list[0] if my_list else None
    for num in my_list:
        max_num = num if num > max_num else max_num
    return max_num
