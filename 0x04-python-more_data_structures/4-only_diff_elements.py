#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """A function that returns a set of all elements present
    in only one set

    Args:
        set_1 (set[str]): first set
        set_2 (set[str]): second set

    Returns:
        set[str]: the symetric difference between set_1 and set_2
    """
    return set_1.symmetric_difference(set_2)
