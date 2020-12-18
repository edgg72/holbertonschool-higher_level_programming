#!/usr/bin/python3
"""find peak"""


def find_peak(list_of_integers):
    """function to find a peak"""
    nums = list_of_integers
    len_ = len(nums)
    if len_ == 0:
        return
    m = len_ // 2
    if (m == len_ - 1 or nums[m] >= nums[m + 1]) and\
       (m == 0 or nums[m] >= nums[m - 1]):
        return nums[m]
    if m != len_ - 1 and nums[m + 1] > nums[m]:
        return find_peak(nums[m + 1:])
    return find_peak(nums[:m])
