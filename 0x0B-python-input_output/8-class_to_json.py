#!/usr/bin/python3
"""Holds only one function,
def class_to_json(obj)"""


def class_to_json(obj):
    """returns the dictionary description
    with simple data structure"""
    return obj.__dict__
