#!/usr/bin/python3
"""
script that takes in a URL, sends a request
to the URL and displays the body of the response
"""
from urllib import request, error
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    try:
        req = request.Request(url)
        with request.urlopen(req) as response:
            print(response.read().decode('utf8'))
    except error.HTTPError as e:
        print('Error code:', e.code)
