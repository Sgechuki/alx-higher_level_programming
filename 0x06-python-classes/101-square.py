#!/usr/bin/python3
"""This module creates class Square
optional private instance attribute size and
Public instance method area"""


class Square:
    """This class defines a square
        Attrinutes:
        size (int, optional):
        Must be integer, otherwise raise a TypeError exception.
        If size is less than 0, raise a ValueError exception
        position (tuple, optional):
        must be a tuple of 2 positive integers, otherwise raise a TypeError
        exception"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes object."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves postion"""
        return self.__position

    @position.setter
    def position(self, value):
        """Does validation before setting postion attribute"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for k in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    def __str__(self):
        """prints square"""
        if self.__size == 0:
            return ""
        sq = ""
        for i in range(self.__position[1]):
            sq = sq + "\n"
        for j in range(self.__size):
            for k in range(self.__position[0]):
                sq = sq + " "
            for m in range(self.__size):
                sq = sq + "#"
            sq = sq + "\n"
        return sq[:-1]
