#!/usr/bin/python3
"""square class."""


class Square:
    """square"""
    def __init__(self, size=0):
        """Constructor.

        Args:
            size: side length of the square

        Raises:
            TypeError: if size if not an int
            ValueError: if size is negative
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """finds the area of a square

        Returns:
            the area of the square
        """
        return (self.__size ** 2)
