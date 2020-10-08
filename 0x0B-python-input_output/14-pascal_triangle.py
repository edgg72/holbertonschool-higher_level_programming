#!/usr/bin/python3
"""
Pascal triangle
"""


def pascal_triangle(n):
    """displays n lines of pascal triangle"""
    triangle = []
    if n <= 0:
        return triangle
    for i in range(n):
        triangle.append([])
        triangle[i].append(1)
        for j in range(1, i):
            triangle[i].append(triangle[i-1][j-1]+triangle[i-1][j])
        if(n != 0):
            triangle[i].append(1)
    return triangle
