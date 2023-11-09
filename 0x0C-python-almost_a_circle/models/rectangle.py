#!/usr/bin/python3
"""This module holds the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Inherits from Base and defines a rectangle
    Args
        width: Private instance attribute
        height: Private instance attribute
        x: Private instance attribute
        y: Private instance attribute
        id: Private instance attribute
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes rectangle instance with attr"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) is not int:
            m = "width must be an integer"
            raise TypeError(m)
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """return height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """return x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """return y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle
        instance with the character #"""
        for n in range(self.__y):
            print()
        for i in range(self.__height):
            for m in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """implement print()"""
        snt = "[Rectangle] ({}) ".format(self.id)
        snt += "{}/{} ".format(self.__x, self.__y)
        snt += "- {}/{}".format(self.__width, self.__height)
        return snt

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute:"""
        attr = ["id", "width", "height", "x", "y"]
        values = [arg for arg in args]
        if len(values) > 0:
            for i in range(len(values)):
                self.__setattr__(attr[i], values[i])
        else:
            for key, val in kwargs.items():
                self.__setattr__(key, val)

    def to_dictionary(self):
        """returns the dictionary representation
        of a Rectangle"""
        d = dict()
        d["width"] = self.width
        d["height"] = self.height
        d["x"] = self.x
        d["y"] = self.y
        d["id"] = self.id
        return d
