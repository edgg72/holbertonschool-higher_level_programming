#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    if my_list:
        for i in my_list:
            if i % 2:
                new.append(False)
            else:
                new.append(True)
    return new
