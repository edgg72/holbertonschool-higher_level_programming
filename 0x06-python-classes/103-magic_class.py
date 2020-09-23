#!/usr/bin/python3
"""Defines the class"""
import math


class MagicClass:
    """A circle"""
    def __init__(self, radius=0):
        """Initializing"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculating area"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculating circumference"""
        return 2 * math.pi * self.__radius
