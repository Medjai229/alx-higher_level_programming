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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        this method writes the JSON string representation of list_objs
        to a file
        """
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                l_objs = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(l_objs))

    @staticmethod
    def from_json_string(json_string):
        """
        this method returns the list of the JSON string
        representation json_string
        """
        if json_string is None:
            return []
        else:
            return loads(json_string)
