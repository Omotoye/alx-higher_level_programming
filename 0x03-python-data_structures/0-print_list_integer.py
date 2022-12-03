#!/usr/bin/python3


def print_list_integer(my_list=[]) -> None:
    """A function to print all the items contained in a given list`

    Args:
        my_list (list[int], optional): list to be printed. Defaults to [].
    """
    for item in my_list:
        print("{}".format(item))
