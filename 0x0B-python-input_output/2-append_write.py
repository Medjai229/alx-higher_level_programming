#!/usr/bin/python3

"""
File: 2-append_write.py
Description: this module contains one function append_write
"""


def append_write(filename="", text=""):
    """
    a function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as my_file:
        my_file.write(text)

    return len(text)
