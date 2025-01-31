#!/usr/bin/python3
"""
Contains a Python script that takes in a URL and an email
sends a POST request to the passed URL with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":

    the_url = sys.argv[1]
    e_mail = sys.argv[2]
    values = {'email': e_mail}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(the_url, data)

    with urllib.request.urlopen(req) as response:
        content = response.read()
    print(content.decode('utf-8'))
