#!/usr/bin/python3

"""
File: 2-is_same_class.py
Description: This module contains one funtion is_same_class
"""


def is_same_class(obj, a_class):
    """
    a function that returns True if the object is exactly an instance
    of the specified class otherwise False.
    """
    return type(obj) == a_class
