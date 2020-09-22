#!/usr/bin/python3
"""definition of Square class"""


class Square:
    """Represents a square
    Attributes:
        __size: size of a square side
    """
    def __init__(self, size=0):
        """Initializes a square
        Args:
            size: size of a square side
        Returns: None
        """
        self.size = size

    def area(self):
        return (self.__size) ** 2

    @property
    def size(self):
        return self.__size

    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
