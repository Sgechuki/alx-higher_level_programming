#!/usr/bin/python3
"""This module holds class Recatngle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from the BaseGeometry class
    Args:
        width (int): breath of rectangle
        height (int): height of rectangle
    """
    def __init__(self, width, height):
        """Initialises object"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """return area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """prints"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
