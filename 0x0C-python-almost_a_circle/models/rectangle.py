#!/usr/bin/python3
"""
This module contains:
1. A class Rectangle that inherits from Base
2. Private instance attributes width and height
   each with its own public getter and setter
3. A class constructor: def __init__(self, width, height, x=0, y=0, id=None):
   Calls the super class with id - this super call with use the logic
   of the __init__ of the Base class
"""
from models.base import Base


class Rectangle(Base):
    """
    A class Rectangle that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor
        It calls the superclass with id for id assignments
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for the width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Setter for the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Setter for the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for X
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        Setter for X
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Setter for y
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        Setter for y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the area of the rectangle instance
        """
        return (self.__width * self.__height)

    def display(self):
        """
        Prints in stdout the Rectangle instance with the character #
        """
        for p in range(self.__y):
            print(" ")
        for i in range(self.__height):
            for q in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """
        Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        an end-user oriented rectangle representation
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                        self.__y, self.__width,
                                                        self.__height))

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute
        """
        attributes = ['id', 'width', 'height', 'x', 'y']

        if args:
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle
        """
        rep = {
               'x': self.x,
               'y': self.y,
               'id': self.id,
               'height': self.height,
               'width': self.width
               }
        return (rep)
