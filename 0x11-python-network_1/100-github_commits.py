#!/usr/bin/python3
"""
Contains a python script that list 10 commits
(from the most recent to oldest) of the repository
“rails” by the user “rails”
"""
import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = "https://api.github.com/repos/" + owner + "/" + repo + "/commits"

    headers = {'Accept': 'application/vnd.github+json',
               'X-GitHub-Api-Version': '2022-11-28'
               }

    req = requests.get(url, headers=headers)
    decoded = req.json()
    i = 0
    for item in decoded:
        commit = item.get('commit')
        author = commit.get('author')
        print(f"{item.get('sha')} {author.get('name')}")
        i += 1
        if i == 10:
            break
