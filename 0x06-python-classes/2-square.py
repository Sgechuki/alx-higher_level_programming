#!/usr/bin/python3
"""This module creates class Square
and optional private instance attribute size"""


class Square:
    """This class defines a square
        Attrinutes:
        size (int, optional):
        Must be integer, otherwise raise a TypeError exception.
        If size is less than 0, raise a ValueError exception"""
    def __init__(self, size=0):
        """Initializes object."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
