#!/usr/bin/python3
"""Improved `Square` class definition with helper method and class property

This module defines a class `Square` based on the module `3-square.py`, it is
an extension of the minimal square class that was defined in the said module.
In this module:
    1. a helper method called `_size_initializer()` was defined to check
        and initialize the given size.
    2. a `size` property was created so as to read the size of the created
        object and a setter is attached to the property to set a new size.

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
        """
        self.__size = 0
        self._size_initializer(size)

    @property
    def size(self) -> int:
        """A Getter for the private `__size` attribute

        Returns:
            int: the private attribute `__size`
        """
        return self.__size

    @size.setter
    def size(self, size: int) -> None:
        """A Setter for the private attribute `__size`

        Args:
            size (int): the given size to set the private attribute
                `__size` to.
        """
        self._size_initializer(size)

    def _size_initializer(self, size: int) -> None:
        """This helper method checks if the given size is an integer and
        it's not less than 0. If this is both true, it assigns the given
        size to the object private variable `__size`, otherwise raises
        an Exception

        Args:
            size (int): the given size to check and assign

        Raises:
            ValueError: Exception raise when the given `size` is less than 0
            TypeError: Exception raise when the given `size` is not an integer
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self) -> int:
        """This method computes and returns the area of the current square
        object

        Returns:
            int: the square of the calling object
        """
        return self.__size**2
