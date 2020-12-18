#!/usr/bin/python3
"""find peak"""


def find_peak(list_of_integers):
    """function to find a peak"""
    peak = 0
    for i in list_of_integers:
        if i > peak:
            peak = i
    if peak == 0:
        return None
    return peak
