#!/usr/bin/python3
"""This module creates class Square
optional private instance attribute size and
Public instance method area"""


class Square:
    """This class defines a square
        Attrinutes:
        size (int, optional):
        Must be integer, otherwise raise a TypeError exception.
        If size is less than 0, raise a ValueError exception"""
    def __init__(self, size=0):
        """Initializes object."""
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size * self.__size

    @property
    def size(self):
        """Retrieves size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Does the validation before setting size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __eq__(self, other):
        """Enable equal comaprison"""
        if self.area() == other.area():
            return True
        else:
            return False

    def __ne__(self, other):
        """Enable not equal to comparison between class Square objects"""
        if self.area() != other.area():
            return True
        else:
            return False

    def __gt__(self, other):
        """Enable greater than comparison between class Square objects"""
        if self.area() > other.area():
            return True
        else:
            return False

    def __ge__(self, other):
        """Enable >= comparison between class Square objects"""
        if self.area() >= other.area():
            return True
        else:
            return False

    def __lt__(self, other):
        """Enable less than comparison between class Square objects"""
        if self.area() < other.area():
            return True
        else:
            return False

    def __le__(self, other):
        """Enable <= comparison between class Square objects"""
        if self.area() <= other.area():
            return True
        else:
            return False
