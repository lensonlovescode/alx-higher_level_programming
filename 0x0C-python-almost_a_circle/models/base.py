#!/usr/bin/python3
"""
This module contains a Class Base with:
1. private class attribute __nb_objects
2. class constructor: def __init__(self, id=None):

This class will be the “base” of all other classes in this project.
The goal of it is to manage id attribute in all your future classes
and to avoid duplicating the same code (by extension, same bugs)
"""


class Base:
    """
    This class is be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code (by extension, same bugs)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor, initializes id
        if id is none, nb_objects is incremented by 1
        Else,public instance attribute is id
        """
        if id not is None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
