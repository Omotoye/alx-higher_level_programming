#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    """A function that returns a list with all values multiplied by a
    number without using any loops

    Args:
        my_list (list[int], optional): the list to multiple its items
            with the given number to create a new list . Defaults to [].
        number (int, optional): the number to multiple the items of the
            given list by to create a new list. Defaults to 0.

    Returns:
        list[int]: new list crated after multiplying all the items of the
            given list by the given number.
    """
    return list(map(lambda x: x * number, my_list))
