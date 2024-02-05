#!/usr/bin/python3

"""
File: 1-my_list.py
Description: This module contains one class MyList
"""


class MyList(list):
    """
    a class that inherits from list
    """
    def __init__(self):
        """
        this method initializes the object with the superclass init
        """
        super().__init__()

    def print_sorted(self):
        """
        this method prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
