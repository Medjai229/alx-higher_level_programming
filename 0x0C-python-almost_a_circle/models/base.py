#!/usr/bin/python3

"""
File: base.py
Description: this module contains one class Base
"""
from json import dumps, loads


class Base:
    """
    This class will be the “base” of all other classes in this project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor
        """
        if id == 0 or id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        this method returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return dumps(list_dictionaries)
