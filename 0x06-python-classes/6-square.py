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
    def size(self, new_size):
        if type(new_size) is not int:
            raise TypeError('size must be an integer')
        if new_size < 0:
            raise ValueError('size must be >= 0')
        self.__size = new_size

    @property
    def position(self):
        """set the position of the printed square"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """finds the area of a square

        Returns:
            the area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """prints a sqaure"""
        if self.size == 0:
            print()
            return

        [print() for i in range(self.position[1])]
        for i in range(self.size):
            [print (" ", end='') for j in range(self.position[0])]
            [print ("#", end='') for k in range(self.size)]
            print()
