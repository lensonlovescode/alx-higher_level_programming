#!/usr/bin/python3
"""
This module defines a class Student that defines a student by:
Public instance attributes:
1. first_name
2. last_name
3. age
It also defines a public method def to_json(self, attr=""):
that retrieves a dictionary representation of a Student instance
with the attributes to be retrieved specified in the attr list of strings
if not specified return all attributes
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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        If attrs is a list of strings:
            only attribute names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved
        """
        if attrs is None:
            return (self.__dict__)
        else:
            dic = {key: value for key, value in
                   self.__dict__.items() if key in attrs}
            return (dic)

    def reload_from_json(self, json):
        """
        This method replaces all attributes of the Student instance
        """
        for key, value in json.items():
            if key == "first_name":
                self.first_name = value
            elif key == "last_name":
                self.last_name = value
            elif key == "age":
                self.age = value
