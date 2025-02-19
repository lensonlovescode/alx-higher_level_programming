#!/usr/bin/python3
"""
Contains a Python script that takes in a URL
sends a request to the URL and displays the body of the response
"""
import sys
import urllib.request
from urllib.error import HTTPError


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            content = response.read()
            decoded_content = content.decode('utf-8')
        print(decoded_content)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
