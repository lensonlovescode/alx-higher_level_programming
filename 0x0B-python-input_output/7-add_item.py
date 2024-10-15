#!/usr/bin/python3
"""
This is a script that adds all arguments
to a Python list, and then save them to a file
"""
import sys


if __name__ == "__main__":

    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    length = len(sys.argv)
    i = 1
    my_list = []
    saved_list = []
    while (i < length):
        my_list.append(sys.argv[i])
        i += 1
    try:
        saved_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        saved_list = []
    for item in my_list:
        saved_list.append(item)
    save_to_json_file(saved_list, "add_item.json")
