#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0) -> int:
    """A function that prints the first `x` elements of a list and
    only integers.

    Args:
        my_list (List[Any], optional): given list of any type.
            Defaults to [].
        x (int, optional): the number of elements to be printed
            from the given list. Defaults to 0.

    Returns:
        int: the real number of integers printed
    """
    integers_printed: int = 0
    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end="")
            integers_printed += 1
        except (ValueError, TypeError):
            pass
        except IndexError:
            raise
    print()
    return integers_printed
