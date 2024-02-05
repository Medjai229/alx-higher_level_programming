#!/usr/bin/python3

"""
File: 11-square.py
Description: this module contains one class Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    a class Square that inherits from Rectangle
    """
    def __init__(self, size):
        """
        a method instantiation with size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
