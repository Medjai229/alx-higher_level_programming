#!/usr/bin/python3

"""
File: 9-rectangle.py
Description: This module contains a subclass Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    a class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        a method instantiation with width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        a method that computs the area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        String representation method
        """
        return ("[" + str(self.__class__.__name__) + "] " +
                str(self.__width) + "/" + str(self.__height))
