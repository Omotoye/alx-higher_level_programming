#!/usr/bin/python3
"""A function that check if an object is an instance of a specified class

.. moduleauthor:: Omotoye Shamsudeen Adekoya

"""


def is_same_class(obj, a_class):
    """A function that returns `True` if the object is exactly an instance
    of a specified class; otherwise `False`

    Args:
        obj (object): object to check against the specified class
        a_class (class): the specified class to check against the object

    Returns:
        bool: True if the object is exactly an instance of the specified class
            False otherwise.
    """
    return True if type(obj) == a_class else False
