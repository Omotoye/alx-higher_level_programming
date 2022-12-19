#!/usr/bin/python3


def safe_print_list(my_list=[], x=0) -> int:
    """A function that prints a given number of elements of a
    given list

    Args:
        my_list (List[Any], optional): The given list to be printed
            from. Defaults to [].
        x (int, optional): the number of elements to print from the
            given list. Defaults to 0.

    Returns:
        int: the real number of elements printed
    """
    elements_printed: int = 0
    for index in range(x):
        try:
            print("{}".format(my_list[index]), end="")
            elements_printed += 1
        except IndexError:
            break
    print()
    return elements_printed
