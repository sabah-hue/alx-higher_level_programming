#!/usr/bin/python3
""" module """


def is_same_class(obj, a_class):
    """ check if the object is exactly an instance of this class """
    if  type(obj) is a_class:
        return True
    return False
