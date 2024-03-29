#!/usr/bin/python3

"""
File: 4-from_json_string.py
Description: this module contains one function from_json_string
"""
import json


def from_json_string(my_str):
    """
    a function that returns an object (Python data structure)
    represented by a JSON string
    """
    return json.loads(my_str)
