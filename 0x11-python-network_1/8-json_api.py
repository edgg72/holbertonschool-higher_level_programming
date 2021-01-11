#!/usr/bin/python3
"""
script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
from sys import argv


if __name__ == "__main__":
    l = ''
    if len(argv) > 1:
        l = argv[1]
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': l})
    try:
        req_data = req.json()
        if not req_data:
            print("No result")
        else:
            print("[{}] {}".format(req_data.get('id'), req_data.get('name')))
    except ValueError:
        print("Not a valid JSON")
