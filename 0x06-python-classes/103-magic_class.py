#!/usr/bin/python3
import math


class MagicClass:

    def __int__(self, radius=0):
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """finds the area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """finfs the circumference"""
        return self.__radius * math.pi * 2
