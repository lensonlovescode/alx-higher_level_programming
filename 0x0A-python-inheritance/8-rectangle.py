#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
This module contains a class Rectangle that inherits
fr0m BaseGeometry in 7-base_geometry.py
"""


class Rectangle(BaseGeometry):
    """
    This class contains an initializtion method
    initiating with width and height
    """
    def __init__(self, width, height):
        """
        The instantinuatoir
        Instantiation with width and height
        width and height must be private. No getter or setter
        width and height must be positive integers
        validated by integer_validator
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.width = width
        self.height = height
