#!/usr/bin/python3
"""This module contains function,
def write_file(filename="", text="")
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and
    returns the number of characters written"""
    with open(filename, "w", encoding="utf-8") as f:
        i = f.write(text)
    return (i)
