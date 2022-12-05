#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """A function that prints a matrix of integer

    Args:
        matrix (list[list[int]], optional): The matrix of integer to be
            printed. Defaults to [[]].
    """
    for row in matrix:
        if row:
            for n in row:
                print("{:d}{}".format(n, "\n" if n is row[-1] else " "), end="")
        else:
            print()
