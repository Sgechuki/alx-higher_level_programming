#!/usr/bin/python3
"""This module creates class Square
and private instance attribute size"""


class Square:
    """Class Square defines a square
        Attributes:
            size (no type): Private instance attribute.
    """

    def __init__(self, size):
        """Initializes the object with size attribute"""
        self.__size = size
