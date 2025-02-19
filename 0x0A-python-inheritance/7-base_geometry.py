#!/usr/bin/python3
"""
This module contains a class BaseGeometry
that raises an Exception with the message
area() is not implemented
"""


class BaseGeometry():
    """
    This class contains a method that raises
    an Exception with the message
    area() is not implemented
    """
    def area(self):
        """
        This method raises an Exception with the message
        area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value:
        value must be an integer, otherwise:
        raise a TypeError exception
        if value is less or equal to 0:
        raise a ValueError exception
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
