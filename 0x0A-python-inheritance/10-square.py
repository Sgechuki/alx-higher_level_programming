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
