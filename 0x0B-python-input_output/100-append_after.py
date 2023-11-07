#!/usr/bin/python3
"""This module holds only one function,
def append_after(filename="", search_string="", new_string="")"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file,
    after each line containing a specific string"""
    new = []
    with open(filename, "r", encoding="utf-8") as f:
        fl = f.readlines()
        for line in fl:
            new.append(line)
            if search_string in line:
                new.append(new_string)
    new = "".join(new)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(new)
