#!/usr/bin/python3


def safe_print_integer(value) -> bool:
    """A function that prints an integer with format method
    if the value given is an integer

    Args:
        value (Any): value to be printed and it could be of
            any type

    Returns:
        bool: `true` if `value` has been correctly printed (which
            means the given `value` is an integer)
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False
