#!/usr/bin/python3
"""This module holds class MyInt"""


class MyInt(int):
    """inherits from int class"""

    def __eq__(self, other):
        """inverts equal to comparison"""
        return super().__ne__(other)

    def __ne__(self, other):
        """inverts not equal operator"""
        return super().__eq__(other)
