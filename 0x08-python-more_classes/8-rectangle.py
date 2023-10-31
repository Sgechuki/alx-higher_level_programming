#!/usr/bin/python3
"""
This module creates a Class Rectangle
"""


class Rectangle:
    """Defines a rectangle
    Attr:
    width (int, optional): Private instance attribute
    height (int, optional): Private instance attribute
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes new object with attributes"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Returns width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets value of width after validating
        its integer and >= 0"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets value of height after validating
        value is of int type and >= 0"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ print the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for h in range(self.__height):
            for i in range(self.__width):
                rect = rect + str(self.print_symbol)
            rect = rect + "\n"
        return rect[:-1]

    def __repr__(self):
        """return a string representation of the rectangle to
        be able to recreate a new instance by using eval()"""
        h = self.__height
        w = self.__width
        return "Rectangle(" + str(w) + ", " + str(h) + ")"

    def __del__(self):
        """Terminates instance"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method that returns the biggest
        rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1
