#!/usr/bin/python3
"""
This modulecontains a function that returns True
if the object is an instance of, or if the object
is an instance of a class that inherited fr0m,
the specified class otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    This is a function that returns True if the object
    is an instance of, or if the object is an instance
    of a class that inherited fr0m, the specified class
    otherwise False.
    """
    return (isinstance(obj, a_class))
