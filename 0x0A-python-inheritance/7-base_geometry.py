#!/usr/bin/python3
"""
BaseGeometry class
"""


class BaseGeometry:
    """
    it raises an exception saying that area() is not implemented
    """
    def area(self):
        """not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that argument is in fact an integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
