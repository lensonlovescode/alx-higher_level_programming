#!/usr/bin/python3
"""
adds two integers
a and b must be integers or floats otherwise raise a TypeError exception
a and b must be first casted to integers if they are float
"""


def add_integer(a, b=98):
    """
    adds two integers together
    """
    if not isinstance(a, (int, float)):
        raise ValueError("a must be an integer or b must be an integer")
    if not isinstance(b, (int, float)):
        raise ValueError("a must be an integer or b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
