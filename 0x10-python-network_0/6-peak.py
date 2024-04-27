#!/usr/bin/python3
"""
The function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    return a peak in a list of unsorted integers
    """
    if list_of_integers == []:
        return None

    size = len(list_of_integers)

    if size < 3:
        return (max(list_of_integers))

    max_idx = int(size / 2)
    peak = list_of_integers[max_idx]

    if peak > list_of_integers[max_idx - 1] and peak > list_of_integers[max_idx + 1]:
        return peak
    elif peak < list_of_integers[max_idx - 1]:
        return find_peak(list_of_integers[:max_idx])
    elif peak <= list_of_integers[max_idx + 1]:
        return find_peak(list_of_integers[max_idx + 1:])
