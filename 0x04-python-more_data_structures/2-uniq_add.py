#!/usr/bin/python3


def uniq_add(my_list=[]) -> int:
    """A function that adds all unique integers in a list (only
    once for each integer).

    Args:
        my_list (list[int], optional): the for which the unique items
            would be added. Defaults to [].

    Returns:
        int: the summation of the unique integers in the given list
    """
    return sum(set(my_list))
