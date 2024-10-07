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
        """
        Initialize a new Rectangle.
        width is the width of the new rectangle.
        height is the height of the new rectangle.
        """
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

    def area(self):
        """
        Returns the area of the rectangle
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
        Return the perimeter of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """
        Returns a string rep of the rectangle using  #
        """
        if self.__height == 0 or self.__width == 0:
            return ("")
        my_list = []
        for j in range(self.__height):
            for i in range(self.__width):
                my_list.append('#')
            if j != self.__height - 1:
                my_list.append('\n')
        return (''.join(my_list))

    def __repr__(self):
        """
        Returns a string representation of the
        rectangle that can be used to recreate
        a new instance using eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
