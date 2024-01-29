#!/usr/bin/python3
"""
File: 0-rectangle.py
Description: defines a class called Rectangle
"""


class Rectangle:
    """
    this is a class defination called Rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        this method retrives the value of attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        this method sets the value of the attribute width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        this method retrives the value of attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        this method sets the value of the attribute height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        this method returns the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        this method returns the perimeter of the rectangele
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        printable string representation of an object of class rectangle
        """
        ret_val = ""

        if self.__height == 0 or self.__width == 0:
            return ret_val

        for i in range(self.__height):
            for j in range(self.__width):
                ret_val += str(self.print_symbol)
            if i < self.__height - 1:
                ret_val += "\n"

        return ret_val

    def __repr__(self):
        """
        Offical string reptresentation of an object of class rectangle
        """
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """
        a special method defines the actions that will be taken when
        an instance is getting deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
