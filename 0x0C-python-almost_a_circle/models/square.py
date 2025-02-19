#!/usr/bin/python3
"""
This module contains a class Square that inherits from Rectangle
This class Square has the same attributes and same methods.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class Square that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor
        Makes a super call will use the logic of the __init__ of
        the Rectangle class.
        The width and height is be assigned to the value of size
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns [Square] (<id>) <x>/<y> - <size>
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.width))

    @property
    def size(self):
        """
        Getter for the square size
        """
        return (self.width)

    @size.setter
    def size(self, value):
        """
        Setter for the square size
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assigns attributes:
        *args is the list of arguments - no-keyworded arguments
         - 1st argument should be the id attribute
         - 2nd argument should be the size attribute
         - 3rd argument should be the x attribute
         - 4th argument should be the y attribute
        kwargs is skipped if *args exists and is not empty
        Each key in this dictionary represents an attribute to the instance
        """
        attributes = ['id', 'size', 'x', 'y']

        if args:
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square
        """
        rep = {
               'id': self.id,
               'x': self.x,
               'size': self.size,
               'y': self.y
               }
        return (rep)
