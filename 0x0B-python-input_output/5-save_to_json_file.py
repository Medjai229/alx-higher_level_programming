#!/usr/bin/python3

"""
File: 5-save_to_json_file.py
Description: this module contains one function save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a text file using a JSON representation
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        my_file.write(json.dumps(my_obj))
