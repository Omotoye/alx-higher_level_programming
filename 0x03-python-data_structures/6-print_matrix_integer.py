#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """A function that prints a matrix of integer

    Args:
        matrix (list[list[int]], optional): The matrix of integer to be
            printed. Defaults to [[]].
    """
    for rw in matrix:
        if rw:
            for n in rw:
                print("{:d}{}".format(n, "\n" if n is rw[-1] else " "), end="")
        else:
            print()
