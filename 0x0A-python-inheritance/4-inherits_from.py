#!/usr/bin/python3
""" module ... """


def inherits_from(obj, a_class):
    """ Only sub class of  """
    return isinstance(obj, a_class) and type(obj) != a_class
