#!/usr/bin/python3
"""
Module contains a function that returns True if the object is
exactly an instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    This function returns True if the object is exactly
    an instance of the specified class ; otherwise False.
    """
    return (isinstance(obj, a_class) and type(obj) == a_class)
