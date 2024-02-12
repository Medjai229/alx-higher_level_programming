#!/usr/bin/python3

"""
File: rectangle.py
Description: this module contains one class Rectangle
            that that inherits from Base in base.py
"""
from models.base import Base


class Rectangle(Base):
    """
    This class represents a rectangle and it inherits from Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        getter method for width attr
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter method for width attr
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
        getter method for height attr
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter method for height attr
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
        getter method for x attr
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter method for x attr
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
        getter method for y attr
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter method for y attr
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        The method computs the area of the rectangle
        """
        return self.__width * self.__height
