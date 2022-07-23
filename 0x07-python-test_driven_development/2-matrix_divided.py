#!/usr/bin/python3i
"""This is the 2-matrix_divided module
    It supplies one function:
    def matrix_divided(matrix, div)
"""

def matrix_divided(matrix, div):
    """divides all elements of a matrix"""
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if type(row) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for c in row:
            if type(c) not in [int, float]:

