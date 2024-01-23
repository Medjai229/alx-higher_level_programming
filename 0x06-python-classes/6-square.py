#!/usr/bin/python3
"""square class."""


class Square:
    """square"""
    def __init__(self, size=0, position=(0, 0)):
        """Constructor.

        Args:
            size: side length of the square
            positon: position of the printed square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """property for the side length

        Raises:
            TypeError: if size if not an int
            ValueError: if size is negative
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """set the position of the printed square"""
        return self.__position

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(num, int) for num in value) and
                all(num >= 0 for num in value)):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """finds the area of a square

        Returns:
            the area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """prints a sqaure"""
        if self.size == 0:
            print("")
            return

        for y in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end='')
            for j in range(self.__size):
                print("#", end='')
            print("")
