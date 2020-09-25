#!/usr/bin/python3
"""
3-say_my_name module
this module prints first name and last name given

"""


def say_my_name(first_name, last_name=""):
    """
    prints first name and last name given
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
