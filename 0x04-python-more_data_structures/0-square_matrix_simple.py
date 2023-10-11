#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        nested = [col * col for col in row]
        new_matrix.append(nested)
    return new_matrix
