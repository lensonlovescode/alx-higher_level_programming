#!/usr/bin/python3
"""
This module contains a function that reads a file
and prints the contents to the std ouptut
"""


def read_file(filename=""):
    """
    This function reads a files contents and prints them
    to the standard output
    """
    with open(filename, encoding='utf-8') as my_file:
        print(my_file.read(), end="")
