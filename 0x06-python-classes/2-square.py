#!/usr/bin/python3
"""
This module creates a class named square that defines a square
with: Private instance attribute: size
      Instantiation with size (no type/value verification
"""


class Square:
    """
    This is an empty class Square that defines a square
    """
    def __init__(self, size=0):
        """
        initialize the class, instantiation with
        optional size: def __init__(self, size=0):

        size must be an integer, otherwise raise
        a TypeError exception with the message
        size must be an integer

        if size is less than 0, raise a ValueError
        exception with the message size must be >= 0
        """

        if not isinstance(size, int):
            raise ValueError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
