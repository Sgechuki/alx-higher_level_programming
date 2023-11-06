#!/usr/bin/python3
"""This module holds class BaseGeometry"""


class BaseGeometry(object):
    """Inherits from object class"""
    def area(self):
        """raises exception error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """that validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
