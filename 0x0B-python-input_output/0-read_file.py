#!/usr/bin/python3

"""
File: 0-read_file.py
Description: this module contains one function read_file
"""


def read_file(filename=""):
    """
    a function that reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read(), end="")
