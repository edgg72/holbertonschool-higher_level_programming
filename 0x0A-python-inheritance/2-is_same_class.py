#!/usr/bin/python3
"""
contains function is_same_class
"""


def is_same_class(obj, a_class):
    """class is same class"""
    r = type(obj) == a_class
    return r
