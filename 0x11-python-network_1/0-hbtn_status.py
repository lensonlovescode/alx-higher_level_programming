#!/usr/bin/python3
"""
Contains a Python script that fetches https://alx-intranet.hbtn.io/status
using the package urllib
"""
import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as request:
    content = request.read()
    decoded_content = content.decode('utf-8')

print("Body response:")
print(f"\t- type: {type(content)}")
print(f"\t- content: {content}")
print(f"\t- utf8 content: {decoded_content}")
