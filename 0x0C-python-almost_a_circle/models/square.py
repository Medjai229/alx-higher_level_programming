#!/usr/bin/python3

"""
File: square.py
Description: this module contains one class Square
            that that inherits from Rectangle in rectangle.py
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class represents a square and it inherits from Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        getter method for size attr
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter method for size attr
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        the string representation of the square class
        """
        s = "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)
        return s

    def update(self, *args, **kwargs):
        """
        this method assigns an argument to each attribute
        """
        if args:
            key_list = ["id", "size", "x", "y"]

            for i in range(len(args)):
                setattr(self, key_list[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        this method returns the dictionary representation of a Square
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
