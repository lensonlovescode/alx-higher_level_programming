#!/usr/bin/python3
"""
Contains a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests
import requests.exceptions.JSONDecodeError


if __name__ == "__main__":
    try:
        data = {'q': sys.argv[1]}
    except IndexError:
        data = {'q': ""}
    req = requests.post('http://0.0.0.0:5000/search_user', data)

    try:
        dict_result = req.json()
        if dict_result:
            print(f"[{dict_result.get('id')}] {dict_result.get('name')}")
        else:
            print("No result")
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
