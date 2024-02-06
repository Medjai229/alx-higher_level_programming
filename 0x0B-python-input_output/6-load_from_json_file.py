#!/usr/bin/python3

"""
File: 6-load_from_json_file.py
Description: this module contains one function load_from_json_file
"""
import json


def load_from_json_file(filename):
    """
    a function that creates an Object from a “JSON file”
    """
    with open(filename, encoding="utf-8") as my_file:
        return json.loads(my_file)
