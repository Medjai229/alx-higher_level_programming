#!/usr/bin/python3

"""
File: 3-to_json_string.py
Description: this module contains one function to_json_string
"""
import json


def to_json_string(my_obj):
    """
    a function that returns the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
