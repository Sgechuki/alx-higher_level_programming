#!/usr/bin/python3
"""This module holds class Rectangle"""
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
