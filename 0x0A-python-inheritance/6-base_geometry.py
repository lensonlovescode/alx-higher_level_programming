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
