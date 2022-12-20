#!/usr/bin/python3
"""`Square` class definition

This module defines a class `Square` based on the module `0-square.py`, it is
an extension of the empty class that was defined in the said module

.. moduleauthor:: Omotoye Shamsudeen Adekoya

"""


class Square:
    """A Class that defines a square with a given size

    Attributes:
        __size (int): private attribute that stores the size of the `Square`
            object created
    """

    def __init__(self, size: int) -> None:
        """Object Instance initialization with size attribute

        Args:
            size (int): the size of the square object to be created
        """
        self.__size: int = size
