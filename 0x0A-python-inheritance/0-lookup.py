#!/usr/bin/python3
"""A function that returns attributes and methods of an object

This modules returns the list of available attributes and methods of any given
object

.. moduleauthor:: Omotoye Shamsudeen Adekoya

"""


def lookup(obj):
    """A function that returns the list of available attributes and methods of
    an object

    Args:
        obj (object): the object from which to return the available attributes
            and methods.

    Returns:
        List[str]: a list of available attributes and methods
    """
    return dir(obj)
