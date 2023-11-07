#!/usr/bin/python3
"""This module contains the function,
def append_write(filename="", text="")
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
    and returns the number of characters added"""
    with open(filename, "a", encoding="utf-8") as f:
        i = f.write(text)
    return (i)
