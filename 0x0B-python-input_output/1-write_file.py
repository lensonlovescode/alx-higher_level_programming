#!/usr/bin/python3
"""
This module contains a function that writes a string
to a text file (UTF8) and returns
the number of characters written:
"""


def write_file(filename="", text=""):
    """
    this function writes a string to a text file (UTF8)
    and returns the number of characters written:
    """
    with open(filename, 'w', encoding='utf-8') as f:
        nb_written = f.write(text)
    return (nb_written)
