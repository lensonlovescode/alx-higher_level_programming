#!/usr/bin/python3
"""
Thsi module contains a function that:
writes an Object to a text file, using a JSON representation:
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an Object to a text file, using a JSON representation
    """
    with open(filename, 'w') as f:
        return (f.write(json.dumps(my_obj)))
