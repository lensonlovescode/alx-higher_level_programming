#!/usr/bin/python3
"""
Contains a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import sys
import requests


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/users/" + username
    Bearer = "Bearer " + password

    headers = {'Accept': 'application/vnd.github+json',
               'Authorization': Bearer,
               'X-GitHub-Api-Version': '2022-11-28'
               }

    req = requests.get(url, headers=headers)
    info = req.json()
    print(info.get('id'))
