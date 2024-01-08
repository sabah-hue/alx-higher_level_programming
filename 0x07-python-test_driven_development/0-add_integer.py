#!/usr/bin/python3
""" module """


def add_integer(a, b=98):
    """ add two integer or float numbers """
    if isinstance(a, (int, float)):
        if isinstance(b, (int, float)):
            return (int(a) + int(b))
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
