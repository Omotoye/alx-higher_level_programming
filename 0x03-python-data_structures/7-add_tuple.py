#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    """A function tthat adds 2 tuples

    Args:
        tuple_a (tuple[int, int], optional): the first tuple. Defaults to ().
        tuple_b (tuple[int, int], optional): the second tuple. Defaults to ().

    Returns:
        tuple[int, int]: new tuple after addition
    """
    helper_list = []
    for i in range(4):
        if i < 2 and len(tuple_a) > i:
            helper_list.append(tuple_a[i])
        elif i < 2 and len(tuple_a) <= i:
            helper_list.append(0)
        elif i > 1 and len(tuple_b) > i - 2:
            helper_list.append(tuple_b[i - 2])
        elif i > 1 and len(tuple_b) <= i - 2:
            helper_list.append(0)
    return (helper_list[0] + helper_list[2], helper_list[1] + helper_list[3])
