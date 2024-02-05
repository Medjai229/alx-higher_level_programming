#!/usr/bin/python3

"""
File: 100-my_int.py
Description: this module contains one class MyInt
"""


class MyInt(int):
    """
    a class MyInt that inherits from int
    """
    def __eq__(self, value):
        """
        the equal representation of the class
        """
        return self.real != value

    def __ne__(self, value):
        """
        the not equal representation of the class
        """
        return self.real == value
