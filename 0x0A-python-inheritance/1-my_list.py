#!/usr/bin/python3
"""This module holds the subclass MyList"""


class MyList(list):
    """MyList inherits from class list"""
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
