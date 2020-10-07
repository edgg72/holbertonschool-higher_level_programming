#!/usr/bin/python3
"""
to_json_string function
"""

import json


def to_json_string(my_obj):
    """returns the json repr of an object"""
    return json.dumps(my_obj)
