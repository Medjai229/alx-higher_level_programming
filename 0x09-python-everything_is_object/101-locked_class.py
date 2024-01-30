#!/usr/bin/python3
"""
File: 101-locked_class.py
Description: this module contains a single class named LockedClass
"""


class LockedClass:
    """
    A class that prevents the user from dynamically
    creating new instance attributes,
    except if the new instance attribute is called 'first_name'.
    """
    __slots__ = ("first_name",)
