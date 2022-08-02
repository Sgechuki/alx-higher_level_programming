#!/usr/bin/python3
"""This module holds only class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from rectangle and defines square"""
    def __init__(self, size):
        """Initializes object"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """prints"""
        snt = "[{}] ".format(self.__class__.__name__)
        snt += "{}/{}".format(self.__size, self.__size)
        return snt
