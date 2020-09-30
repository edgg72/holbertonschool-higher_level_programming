#!/usr/bin/python3
"""
5-text_indentation module
"""


def text_indentation(text):
    """splits a text into lines"""
    if type(text) != str:
        raise TypeError("text must be a string")
    space_check = 0
    for i in text:
        if space_check == 0:
            if i == ' ':
                continue
            else:
                space_check = 1
        if space_check == 1:
            if i is '.' or i is '?' or i is ':':
                print(i)
                print()
                space_check = 0
            else:
                print(i, end="")
