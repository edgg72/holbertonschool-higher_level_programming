#!/usr/bin/python3
"""
contains function inherits from
"""


def inherits_from(obj, a_class):
    """class inherits from"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
