#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    """A function that deletes the item at a specific postion
    in a list

    Args:
        my_list (list[int], optional): the list to be operated on.
            Defaults to [].
        idx (int, optional): index of the item to be removed.
            Defaults to 0.

    Returns:
        list[int]: the new list after the specified item has
            been removed
    """
    if idx in range(0, len(my_list)):
        del my_list[idx]
    return my_list
