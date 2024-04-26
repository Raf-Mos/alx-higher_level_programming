#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(int_list):
    """Return a peak in a list of unsorted integers."""
    if int_list == []:
        return None

    size = len(int_list)
    if size == 1:
        return int_list[0]
    elif size == 2:
        return max(int_list)

    mid = int(size / 2)
    peak = int_list[mid]
    if peak > int_list[mid - 1] and peak > int_list[mid + 1]:
        return peak
    elif peak < int_list[mid - 1]:
        return find_peak(int_list[:mid])
    else:
        return find_peak(int_list[mid + 1:])
