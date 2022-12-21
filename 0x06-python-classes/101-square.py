#!/usr/bin/python3
"""Improved `Square` class definition with helper method and class property

This module defines a class `Square` based on the module `5-square.py`, it is
an extension of the minimal square class that was defined in the said module.
In this module:
    1. the a method for printing the shape of the square object to stdout
        with `#` was modified to take into account the position the printing
        should be done.
    2. an helper method was added to check if the given position attribute is
        a tuple of two positive integers.

.. moduleauthor:: Omotoye Shamsudeen Adekoya

"""


class Square:
    """A Class that defines a square with a given size

    Attributes:
        __size (int): private attribute that stores the size of the `Square`
            object created
    """

    def __init__(self, size: int = 0, position=(0, 0)) -> None:
        """Initializes the attributes of the `Square` object instance

        Args:
            size (int, optional): the size of the `Square` object
                to be created. Defaults to 0.
            pose (tuple[int, int], optional): tuple of two positive integers.
                to set the position where the shape printing would be done
                Defaults to (0, 0).
        """
        self.__size: int = 0
        self.__position = (0, 0)
        self._size_initializer(size)
        self._position_initializer(position)

    def __str__(self) -> str:
        size: int = self.__size
        pose_x: str = self.__position[0] * " "
        pose_y: str = self.__position[1] * "\n"
        return (pose_y + ((pose_x + ("#" * size) + "\n") * size) if size else "\n")[:-1]


    @property
    def size(self) -> int:
        """A Getter for the private `__size` attribute

        Returns:
            int: the private attribute `__size`
        """
        return self.__size

    @size.setter
    def size(self, value: int) -> None:
        """A Setter for the private attribute `__size`

        Args:
            value (int): the given size to set the private attribute
                `__size` to.
        """
        self._size_initializer(value)

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

    def _position_initializer(self, position):
        """This helper method check if the position given is a tuple of two
        positive integers

        Args:
            position (tuple[int, int]): the position value to check

        Raises:
            TypeError: raises a TypeError if the given position is not a
                tuple of two positive integers.
        """
        is_tuple: bool = isinstance(position, tuple)
        correct_len: bool = len(position) == 2
        if is_tuple and correct_len and position[0] >= 0 and position[1] >= 0:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self) -> int:
        """This method computes and returns the area of the current square
        object

        Returns:
            int: the square of the calling object
        """
        return self.__size**2

    def my_print(self) -> None:
        """A Public instance method to print the shape of the square object
        with `#` to stdout
        """
        size: int = self.__size
        pose_x: str = self.__position[0] * " "
        pose_y: str = self.__position[1] * "\n"
        shape: str = ((pose_x + ("#" * size) + "\n") * size) if size else "\n"
        print("{}{}".format(pose_y, shape), end="")
