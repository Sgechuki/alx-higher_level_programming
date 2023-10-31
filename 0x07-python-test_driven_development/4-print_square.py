#!/usr/bin/python3
"""This is the 4-print_square.py module
It supplies only one function:
    print_square(size):
"""


def print_square(size):
    """ prints a square with the character #"""
    if type(size) != int:
        if type(size) == float and size < 0:
            raise TypeError("size must be an integer")
        else:
            raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
