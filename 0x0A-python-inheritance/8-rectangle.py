#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""This module holds the class Rectangle"""


class Rectangle(BaseGeometry):
    """Inherits from the BaseGeometry class"""
    def __init__(self, width, height):
        """Initialises object"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
