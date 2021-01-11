#!/usr/bin/python3
"""
Sends a request and shows if there is an HTTP error
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    req = get(argv[1])
    try:
        req.raise_for_status()
        print(req.text)
    except:
        print("Error code: {}".format(req.status_code))
