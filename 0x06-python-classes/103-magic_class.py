#!/usr/bin/python3
"""This module implemnts a MagicClass that does exactly
as the bytecode offered by ALX SE"""
import math


class MagicClass:
    """Creates a class MagicClass to define a circle

    Attributes:
    radius(int, float, optional):
    Must be a number (float or integer), otherwise raise
    a TypeError exception"""
    def __init__(self, radius=0):
        """Initializes an MagicClass instance"""

        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """Returns area of the MagicClass"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Retrn circumference of MagicClass"""
        return 2 * math.pi * self.__radius
