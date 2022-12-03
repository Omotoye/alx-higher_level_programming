#!/usr/bin/python3


def element_at(my_list: list[int], idx: int) -> int | None:
    """A function to return the item in a given index

    Args:
        my_list (list[int]): the list to be taken from
        idx (`int`): the idenx of the item to be returned

    Returns:
        int | None: None if there's a problem with the given index,
            int if no problem with the given index
    """
    if idx < 0 or idx > len(my_list) - 1:
        return None
    return my_list[idx]
