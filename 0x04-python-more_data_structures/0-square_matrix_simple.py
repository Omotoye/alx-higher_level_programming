#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """A function that computes the square value of all integers
    of a matrix.

    Type Aliases:
        Matrix = List[List[int]]

    Args:
        matrix (Matrix, optional): The matrix to take all the
            values to be squared for the new matrix to be returned.
            Defaults to [[]].

    Returns:
        Matrix: The new matrix that contains the square values
            from the given matrix
    """
    square_matrix = []
    for row in matrix:
        square_matrix.append(list(map(lambda x: x * x, row)))
    return square_matrix
