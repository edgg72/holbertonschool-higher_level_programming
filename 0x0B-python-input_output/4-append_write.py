#!/usr/bin/python3
"""
the append file function
"""


def append_write(filename="", text=""):
    """returns the number of chars appended to a file"""
    with open(filename, 'a+', encoding='utf8') as f:
        return f.write(text)
