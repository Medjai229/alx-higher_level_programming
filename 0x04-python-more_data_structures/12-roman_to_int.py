#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return (0)

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    result = 0
    prev_val = 0

    for c in reversed(roman_string):
        value = roman_dict[c]
        if value < prev_val:
            result -= value
        else:
            result += value
            prev_val = value

    return (result)
