#!/usr/bin/python3
""" module ... """


def append_write(filename="", text=""):
    """ appends a string at the end of a text file """
    with open(filename, "a") as f:
        return (f.write(text))
