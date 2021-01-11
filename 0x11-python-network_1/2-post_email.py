#!/usr/bin/python3
"""
script that takes in a URL and an email,
sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response
(decoded in utf-8)
"""
from urllib import request, parse
from sys import argv


email = argv[2]
data_dict = {'email': email}
data = parse.urlencode(data_dict).encode('utf-8')

with request.urlopen(argv[1], data) as response:
    print(response.read().decode('utf8'))
