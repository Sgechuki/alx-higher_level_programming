#!/usr/bin/python3
"""This is the 5-text_indentation module, it supplies only one function
    text_indentation(text)
"""


def text_indentation(text):
    """prints a text with 2 new lines after each of
    these characters: ., ? and :"""
    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        new = text.replace(' ?', '?\n').replace(': ', ':\n')
        new = new.replace('. ', '.\n')
        lst = new.split('\n')
        for i in range(len(lst)):
            if i < len(lst) - 1:
                print(lst[i])
                print()
            else:
                print(lst[i], end="")
