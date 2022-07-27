#!/usr/bin/python3
"""This is the 0-add_integer module
The 0-add_integer module supplies one function
add_integer(a, b)."""


def add_integer(a, b=98):
    """Return sum of a and b"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) == float and not a.is_integer():
        raise TypeError("a must be an integer")
    if type(b) == float and not b.is_integer():
        raise TypeError("b must be an integer")
    return int(a) + int(b)
