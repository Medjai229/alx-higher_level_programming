#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for val, key in list(a_dictionary.items()):
        if val == value:
            del a_dictionary[key]

    return (a_dictionary)
