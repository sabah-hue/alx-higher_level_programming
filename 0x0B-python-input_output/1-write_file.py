#!/usr/bin/python3
""" module ... """


def write_file(filename="", text=""):
    """writes a string to file and return number of char"""
    with open(filename, "w") as f:
        return f.write(text)
