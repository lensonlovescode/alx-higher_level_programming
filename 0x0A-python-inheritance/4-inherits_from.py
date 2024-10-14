#!/usr/bin/python3
"""
This module contains a function that returns True
if the object is an instance of a class that inherited
(directly or indirectly) fr0m the specified class
otherwise False.
"""
def inherits_from(obj, a_class):
    """
    This function returns True if the object is
    an instance of a class that inherited
    (directly or indirectly) fr0m the specified class
    otherwise False.
    """
    object_class = type(obj)
    return (issubclass(object_class, a_class) and type(obj) is not a_class)
