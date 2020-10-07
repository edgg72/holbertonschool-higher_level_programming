#!/usr/bin/python3
"""
using three previous functions,
this adds all arguments to a Python list, and then save them to a file
"""

from sys import argv
save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file

file = "add_item.json"

try:
    json_list = load_from_json_file(file)
except:
    json_list = []

for arg in argv[1:]:
    json_list.append(arg)

save_to_json_file(json_list, file)
