#!/usr/bin/python3

"""
File: 10-student.py
Description: this module contains one class Student
"""


class Student():
    """
    a class Student that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Method initialization
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        a method that retrieves a dictionary
        representation of a Student instance
        """
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__

        my_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                my_dict[key] = value

        return my_dict
