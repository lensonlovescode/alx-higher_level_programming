#!/usr/bin/python3
"""
Function that prints a square with the character #.
"""


def print_square(size):
    """
    size is the size length of the square
    size must be an integer, else raise a TypeError exception:
    "size must be an integer"
    if size is less than 0, raise a ValueError exception:
        "size must be >= 0"
    if size is a float and is less than 0:
        raise a TypeError exception: "size must be an integer"
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
