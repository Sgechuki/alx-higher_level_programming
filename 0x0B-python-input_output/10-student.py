#!/usr/bin/python3
"""This module is for class Student"""


class Student:
    """Defines a student by
    Args
    first name: first name of student
    last name: last name of student
    Age: How old the student is

    Instance methdos
    to_json: retrieves a dictionary representation
            of a Student instance
    """
    def __init__(self, first_name, last_name, age):
        """Initialises an object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation"""
        d = self.__dict__
        if attrs is None:
            return d
        else:
            return {key: value for key, value in d.items() if key in attrs}
