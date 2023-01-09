#!/usr/bin/python3
"""A class that inherit and improves the `list` class

This module inherits from list and has a public instance method
`print_sorted()` that prints the list, but sorted (ascending sort)

.. moduleauthor:: Omotoye Shamsudeen Adekoya

"""


class MyList(list):
    """This Class inherits from the `list` Base Class and adds a method
    to print sorted list

    BaseClass:
        list (object): the `list` base class from which this class is
            inheriting from
    """

    def print_sorted(self) -> None:
        """A public class method that prints sorted list
        """
        print(sorted(self))
