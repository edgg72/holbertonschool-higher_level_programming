#!/usr/bin/python3
"""
class Square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a square"""
    def __init__(self, size):
        """instantiation"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns area of square"""
        return self.__size ** 2

    def __str__(self):
        """informal string reepresentation of a square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
