#!/usr/bin/python3
"""
divides a matrix by an integer
x must be a list of lists of integers or floats, otherwise raise a TypeError
Each row of the matrix must be of the same size, otherwise raise a TypeError
div must be a number (integer or float), otherwise raise a TypeError exception
div can’t be equal to 0, otherwise raise a ZeroDivisionError exception
"""


def matrix_divided(matrix, div):
    """
    divides a matrix by an integer
    x must be a list of integers or floats, otherwise raise a TypeError
    Each matrix row must be of the same size, otherwise raise a TypeError
    div must be an integer or float, otherwise raise a TypeError exception
    div can’t be equal to 0, otherwise raise a ZeroDivisionError exception
    """
    length = len(matrix[0])
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    for row in matrix:
        if len(row) is not length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(err_msg)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return([[round((element / div), 2) for element in row] for row in matrix])
