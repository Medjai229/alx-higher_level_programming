#!/usr/bin/python3

"""
File: 100-append_after.py
Description: this module contains one function append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """
    a function that inserts a line of text to a file
    after each line containing a specific string
    """
    with open(filename, encoding="utf-8") as my_file:
        list_lines = my_file.readlines()
        new_content = ""
        for line in list_lines:
            new_content += line
            if search_string in line:
                new_content += new_string

    with open(filename, "w", encoding="utf-8") as my_file:
        my_file.write(new_content)
