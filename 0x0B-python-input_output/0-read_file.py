#!/usr/bin/python3
""" module ... """


def read_file(filename=""):
    """ reads a file (UTF8) and prints to stdout """
    with open(filename, "r") as f:
        print(f.read(), end="")
