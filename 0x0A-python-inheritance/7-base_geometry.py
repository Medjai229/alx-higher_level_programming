#!/usr/bin/python3

"""
File: 7-base_geometry.py
Description: This module contains one class BaseGeometry
"""


class BaseGeometry:
    """
    an class defination
    """
    def area(self):
        """
        this method raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        this method validates a value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
