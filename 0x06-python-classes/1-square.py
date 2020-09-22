#!/usr/bin/python3
"""definition of Square class"""


class Square:
    """Represents a square
    Attributes:
        __size: size of a square side
    """
    __size = None

    def __init__(self, size):
        """Initializes a square
        Args:
            size: size of a square side
        Returns: None
        """
        self.__size = size
