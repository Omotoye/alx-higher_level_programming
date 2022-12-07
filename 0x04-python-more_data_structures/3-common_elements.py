#!/usr/bin/python3


def common_elements(set_1, set_2):
    """A function that returns a set of common elements in two sets

    Args:
        set_1 (set[str]): first set of string
        set_2 (set[str]): second set of string

    Returns:
        set[str]: the intersection of both set_1 and set_2
    """
    return set_1.intersection(set_2)
