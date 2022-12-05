#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]) -> None:
    """A function that prints a matrix of integer

    Args:
        matrix (list[list[int]], optional): The matrix of integer to be
            printed. Defaults to [[]].
    """
    for row in matrix:
        for num in row:
            print("{}{}".format(num, "\n" if num is row[-1] else " "), end="")
