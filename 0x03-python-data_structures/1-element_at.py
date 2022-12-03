#!/usr/bin/python3


def element_at(my_list, idx):
    """A function to return the item in a given index

    Args:
        my_list (list[int]): the list to be taken from
        idx (`int`): the idenx of the item to be returned

    Returns:
        int | None: None if there's a problem with the given index,
            int if no problem with the given index
    """
    if idx not in range(0, len(my_list)):
        return None
    return my_list[idx]
