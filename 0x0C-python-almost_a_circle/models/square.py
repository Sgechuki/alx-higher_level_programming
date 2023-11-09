#!/usr/bin/python3
"""This module holds the Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines square
    Args
        size
        x
        y
        id
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes object with attr"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns size"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets width and hight after validaion"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes"""
        attr = ["id", "size", "x", "y"]
        values = [arg for arg in args]
        hl = len(values)
        if hl > 0:
            for i in range(hl):
                self.__setattr__(attr[i], values[i])
        else:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    def __str__(self):
        """Enables print(obj)"""
        snt = "[{}] ".format(self.__class__.__name__)
        snt += "({}) {}/{} - ".format(self.id, self.x, self.y)
        snt += "{}".format(self.width)
        return snt

    def to_dictionary(self):
        """returns the dictionary
        representation of a Square"""
        dic = dict()
        dic["id"] = self.id
        dic["size"] = self.width
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
