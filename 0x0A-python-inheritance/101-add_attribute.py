#!/usr/bin/python3
""" module ... """


def add_attribute(a, name, value):
    """ add att ... """
    if not hasattr(a, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(a, name, value)
