#!/usr/bin/python3
"""
Mylist  class
"""


class MyList(list):
    """MyList subclass"""
    def __init__(self):
        """instantiation"""
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
