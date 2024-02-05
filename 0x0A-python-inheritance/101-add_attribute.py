#!/usr/bin/python3

"""
File: 101-add_attribute.py
Description: this module contains one function add_attribute
"""


def add_attribute(obj, att, value):
    """
    a function that adds a new attribute to an object if it’s possible
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, att, value)
    else:
        raise TypeError("can't add new attribute")
