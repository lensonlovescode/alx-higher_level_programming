#!/usr/bin/python3
"""
This module contains a function that returns
a list of lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    This function returns a list of lists of integers
    representing the Pascal’s triangle of n:
    """
    big_list = []
    if n <= 0:
        return (big_list)
    for i in range(n):
        big_list.append(list(str(11 ** i)))
    return (big_list)
