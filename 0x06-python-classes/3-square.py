#!/usr/bin/python3
"""Improved `Square` class definition with Exception Handling

This module defines a class `Square` based on the module `2-square.py`, it is
an extension of the minimal square class that was defined in the said module.
In this module a method was added to the `Square` class called `Square.area()`
to compute and return the area of the calling `Square` object.

.. moduleauthor:: Omotoye Shamsudeen Adekoya

"""


class Square:
    """A Class that defines a square with a given size

    Attributes:
        __size (int): private attribute that stores the size of the `Square`
            object created
    """

    def __init__(self, size: int = 0) -> None:
        """Initializes the attributes of the `Square` object instance

        Args:
            size (int, optional): the size of the `Square` object
                to be created. Defaults to 0.

        Raises:
            ValueError: Exception raise when the given `size` is less than 0
            TypeError: Exception raise when the given `size` is not an integer
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size: int = size
        else:
            raise TypeError("size must be an integer")

    def area(self) -> int:
        """This method computes and returns the area of the current square
        object

        Returns:
            int: the square of the calling object
        """
        return self.__size**2
