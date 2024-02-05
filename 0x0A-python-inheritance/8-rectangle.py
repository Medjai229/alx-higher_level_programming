#!/usr/bin/python3

"""
File: 8-rectangle.py
Description: This module contains a subclass Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
   """
   a class Rectangle that inherits from BaseGeometry
   """
   def __init__(self, width, height):
       """
       a method instantiation with width and height
       """
       self.integer_validator("width", width)
       self.integer_validator("height", height)
       self.__width = width
       self.__height = height
