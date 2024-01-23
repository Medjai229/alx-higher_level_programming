#!/usr/bin/python3
"""square class."""


class Square:
    """square"""
    def __init__(self, size=0):
        """Constructor.

        Args:
            size: side length of the square
        """
        self.__size = size

    @property
    def size(self):
        """property for the side length

        Raises:
            TypeError: if size if not an int
            ValueError: if size is negative
        """
        return self.__size

    @size.setter
    def size(self, new_size):
        if type(new_size) is not int:
            raise TypeError('size must be an integer')
        if new_size < 0:
            raise ValueError('size must be >= 0')
        self.__size = new_size

    def area(self):
        """finds the area of a square

        Returns:
            the area of the square
        """
        return (self.__size ** 2)

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()
