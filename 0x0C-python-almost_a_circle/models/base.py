#!/usr/bin/python3
"""
This module contains a Class Base with:
1. private class attribute __nb_objects
2. class constructor: def __init__(self, id=None):

This class will be the “base” of all other classes in this project.
The goal of it is to manage id attribute in all your future classes
and to avoid duplicating the same code (by extension, same bugs)
"""
import json


class Base:
    """
    This class is be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code (by extension, same bugs)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor, initializes id
        if id is none, nb_objects is incremented by 1
        Else,public instance attribute is id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries:
            return (json.dumps(list_dictionaries))
        else:
            return ("[]")

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        rep = [objs.to_dictionary() for objs in list_objs]

        with open(filename, 'w') as f:
            if list_objs:
                f.write(Base.to_json_string(rep))
            else:
                f.write("[]")

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string
        json_string is a string representing a list of dictionaries
        """

        if json_string:
            return (json.loads(json_string))
        else:
            return ([])

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            instance = cls(10, 10)
        else:
            instance = cls(10)
        instance.update(**dictionary)
        return (instance)

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from <Class name>.json - eg: Rectangle.json
        If the file doesn’t exist, it return an empty list
        Otherwise, return a list of instances
        the type of these instances depends on cls
        """
        filename = cls.__name__ + ".json"

        try:
            with open(filename, 'r') as f:
                list_dict = Base.from_json_string(f.read())
                instances = [cls.create(**item) for item in list_dict]
                return (instances)
        except FileNotFoundError:
            return ([])
