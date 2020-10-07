#!/usr/bin/python3
"""
the write file function
"""


def write_file(filename="", text=""):
    """writes to a file overwriting it, creates it if it doesn't exist"""
    with open(filename, 'w', encoding='utf8') as f:
        return f.write(text)
