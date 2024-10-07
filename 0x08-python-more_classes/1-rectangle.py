#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle.
"""


class Rectangle:
    """
    This class Rectangle that defines a rectangle
    height is the height, obviously
    width is the width
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        getter, retrieves the width of the instance
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter, sets the width of the instance to value
        value must be an integer >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter, retrieves & returns height of the instance
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter, sets the height of the instance to value
        value must be an integer >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
