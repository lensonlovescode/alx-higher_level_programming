#!/usr/bin/python3
"""
This module defines a class Student that defines a student by:
Public instance attributes:
1. first_name
2. last_name
3. age
It also defines a public method def to_json(self):
that retrieves a dictionary representation of a Student instance
"""


class Student:
    """
    A class Student that defines a student by attributes:
    first_name, last_name and age
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiation method with first_name, last_name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance
        """
        return (self.__dict__)
