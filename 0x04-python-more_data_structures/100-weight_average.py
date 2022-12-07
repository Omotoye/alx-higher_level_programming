#!/usr/bin/python3


def weight_average(my_list = []) -> float:
    """A function that returns the weighted average of all integers
    tuple `(<score>, <weight>)` 

    Args:
        my_list (list[tuple[int, int]], optional): a list of tuples con. Defaults to [].

    Returns:
        float: _description_
    """
    result = 0.0
    if my_list:
        for tup in my_list:
            result += tup[0] * tup[1]
        result = result / sum([tup[1] for tup in my_list])
    return result
