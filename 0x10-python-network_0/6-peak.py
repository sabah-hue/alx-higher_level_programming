#!/usr/bin/python3
""" finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """find a peak in unsorted list"""
    size = len(list_of_integers)
    if  size == 0:
        return None
    if size == 1:
        return list_of_integers[0]
    if size == 2:
        if list_of_integers[0] > list_of_integers[1]:
            return list_of_integers[0]
        return list_of_integers[1]
    # tmp = list_of_integers[0]
    # for i in list_of_integers:
    #     if tmp < i:
    #         tmp = i
    # return tmp
    #using binary search
    peak = list_of_integers[int(size / 2)]
    if peak > list_of_integers[int(size / 2) - 1] and peak > list_of_integers[int(size / 2) + 1]:
        return peak
    elif peak < list_of_integers[int(size / 2) - 1]:
        return find_peak(list_of_integers[:int(size / 2)])
    else:
        return find_peak(list_of_integers[int(size / 2) + 1:])
