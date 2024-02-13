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

    def display(self):
        """
        this method prints in stdout the Rectangle
        instance with the character #
        """
        for y in range(self.__y):
            print()
        for height in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for width in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        the string representation of the rectangle class
        """
        s = "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)
        return s

    def update(self, *args, **kwargs):
        """
        this method assigns an argument to each attribute
        """
        if args:
            key_list = ["id", "width", "height", "x", "y"]

            for i in range(len(args)):
                setattr(self, key_list[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        this method returns the dictionary representation of a Rectangle
        """
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
