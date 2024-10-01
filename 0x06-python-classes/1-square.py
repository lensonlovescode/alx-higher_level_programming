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
    def __init__(self, size):
        """
        initialize the class
        size - size of the square
        """
        self.__size = size
