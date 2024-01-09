#!/usr/bin/python3
""" module ... """


class MyInt(int):
    """ class MyInt that inherits from int"""
    def __eq__(self, value):
        return int.__ne__(self, value)

    def __ne__(self, value):
        return int.__eq__(self, value)
