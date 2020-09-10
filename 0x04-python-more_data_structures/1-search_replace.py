#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    count = 0
    for i in range(1, len(my_list)):
        if my_list[i] == search:
            new[i] = replace

    return new
