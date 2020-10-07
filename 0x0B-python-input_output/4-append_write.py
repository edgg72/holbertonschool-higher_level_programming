#!/usr/bin/python3
"""
the append file function
"""


def append_write(filename="", text=""):
    with open(filename, 'a+', encoding='utf8') as f:
        return f.write(text)
