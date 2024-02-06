#!/usr/bin/python3

"""
File: 9-student.py
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

    def to_json(self):
        """
        a method that retrieves a dictionary
        representation of a Student instance
        """
        return self.__dict__
