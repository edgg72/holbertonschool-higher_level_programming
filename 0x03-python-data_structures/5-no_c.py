#!/usr/bin/python3
def no_c(my_string):
    _string = ""
    for x in my_string:
        if x != 'c' and x != 'C':
            _string = _string + x
    return _string
