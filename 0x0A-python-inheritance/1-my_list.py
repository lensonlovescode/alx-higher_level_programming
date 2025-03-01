#!/usr/bin/python3
"""
Module defines: Class MyList that inherits from list:
                Public instance method: def print_sorted(self):
                    that prints the list, but sorted (ascending sort)
"""


class MyList(list):
    """
    A class MyList that inherits from list
    """

    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
