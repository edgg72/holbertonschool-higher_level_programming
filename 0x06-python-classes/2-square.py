#!/usr/bin/python3
"""definition of Square class"""


class Square:
    """Represents a square
    Attributes:
        __size: size of a square side
    """
    __size = None

    def __init__(self, size=0):
        """Initializes a square
        Args:
            size: size of a square side
        Returns: None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
