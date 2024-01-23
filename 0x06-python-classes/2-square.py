#!/usr/bin/python3
"""square class."""


class Square:
    """square"""
    def __init__(self, size):
        """Constructor.
        Args:
            size: side length of the square
        Raises:
            TypeError: if size if not an int
            ValueError: if size is negative
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
