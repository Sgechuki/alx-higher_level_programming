#!/usr/bin/python3

"""This is the 2-matrix_divided module
    It supplies one function:
    def matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    m = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(m)
    if not all(isinstance(x, list) for x in matrix):
        raise TypeError(m)
    iof = all(isinstance(y, (int, float)) for x in matrix for y in x)
    if not iof:
        raise TypeError(m)

    size = len(matrix[0])
    sl = all(size == len(x) for x in matrix)
    if not sl:
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(column / div, 2) for column in row] for row in matrix]
