#!/usr/bin/python3
"""
read file function
"""


def read_file(filename=""):
    """ reads a file and prints it"""
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
    print(read_data, end="")
