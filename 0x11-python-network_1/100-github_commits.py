#!/usr/bin/python3
"""
script that takes 2 arguments in order to solve this challenge.
The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
"""

import requests
from sys import argv


if __name__ == '__main__':
    req = requests.get('https://api.github.com/repos/{}/{}/commits'
                       .format(argv[2], argv[1]))
    commits = req.json()
    for commit in commits[:10]:
        print('{}: '.format(commit.get('sha')), end='')
        print(commit.get('commit').get('author').get('name'))
