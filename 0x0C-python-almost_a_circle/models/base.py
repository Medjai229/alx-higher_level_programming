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
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as my_file:
            if list_objs is None:
                my_file.write("[]")
            else:
                for obj in list_objs:
                    l = obj.to_dictionary()
                my_file.write(cls.to_json_string(l))
