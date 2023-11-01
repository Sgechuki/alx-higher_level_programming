#!/usr/bin/python3

"""This is the 2-matrix_divided module
    It supplies one function:
    def matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix"""
    m = "matrix must be a matrix (list of lists) of integers/floats"
    if not all(isinstance(x, list) for x in matrix):
        raise TypeError(m)
    elif not all(isinstance(y, (int, float)) for x in matrix for y in x):
        raise TypeError(m)
    elif not all(len(matrix[0] == len(x) for x in matrix)):
        raise TypeError("Each row of the matrix must have the same size")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(column / div, 2) for column in row] for row in matrix]
