#!/usr/bin/python3

"""
File: 4-inherits_from.py
Description: This module contains one function inherits_from
"""


def inherits_from(obj, a_class):
    """
    a function that returns True if the object is an instance
    of a class that inherited (directly or indirectly) from
    the specified class otherwise False
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
