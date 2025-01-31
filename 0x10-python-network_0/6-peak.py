#!/usr/bin/python3
"""
Contains a function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    A function that finds a peak in a list of unsorted integers.
    """
    try:
        sorted_list = sorted(list_of_integers)
        return (sorted_list[len(list_of_integers) - 1])
    except IndexError:
        pass
