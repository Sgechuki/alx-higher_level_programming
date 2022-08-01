#!/usr/bin/python3
"""This module has only one function, def lookup(obj)"""


def lookup(obj):
    """ returns the list of available attributes and methods of an object"""
    return dir(obj)
