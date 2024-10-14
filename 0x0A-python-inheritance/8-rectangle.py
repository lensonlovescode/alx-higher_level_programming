#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
This module contains a class Rectangle that inherits
fr0m BaseGeometry in 7-base_geometry.py
"""


class Rectangle(BaseGeometry):
    """
    This class contains an initializtion method
    """
    def __init__(self, width, height):
        """
        The instantinuator
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.width = width
        self.height = height
