#!/usr/bin/python3


def safe_print_division(a: int, b: int):
    """A function that divides 2 integers and prints the result

    Args:
        a (int): the first integer (numerator)
        b (int): the second integer (denominator)

    Returns:
        Optional[float]: the result from the division `a/b` if successful,
            otherwise `None`
    """
    result = None
    try:
        result = a / b
    except Exception:
        pass
    finally:
        print("Inside result: {}".format(result))
    return result
