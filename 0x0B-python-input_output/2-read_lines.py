#!/usr/bin/python3
"""
contains the read lines function
"""


def read_lines(filename="", nb_lines=0):
    """read nb_lines from a file"""
    with open(filename, 'r', encoding='utf8') as f:
        if nb_lines <= 0:
            print(f.read())
            return
        for line in range(nb_lines):
            print(f.readline())
