#!/usr/bin/python3

"""
File: 7-add_item.py
Description: a program that adds all arguments to a Python list
and then save them to a file
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

av = list(sys.argv[1:])

try:
    file_content = load_from_json_file('add_item.json')
except Exception:
    file_content = []

file_content.append(av)
save_to_json_file(file_content, 'add_item.json')
