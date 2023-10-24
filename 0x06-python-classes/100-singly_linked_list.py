#!/usr/bin/python3
"""This module creates a class Node that
defines a node of a singly linked list"""


class Node:
    """Defines a node of a singly inked list
    Attributes:
    data(int): Private instance attribute
               Must be an integer, otherwise raise a TypeError exception
    next_node: Private instance attribute
               Can be None or must be a Node, otherwise raise a TypeError exception"""
    def __init__(self, data, next_node=None):
        """Initialize instance with attributes"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrives data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets data after validation"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Retrives next_node attribute"""
        return self__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets next_node after validation"""
        if not isinstance(value, Node) or value != None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

