#!/usr/bin/python3
""" module """


def matrix_divided(matrix, div):
    """ division """
    if type(matrix) is not list or len(matrix) is 0:
        x = "matrix must be a matrix (list of lists) of integers/floats")
        raise TypeError(x)

    div_matrix = []
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div is 0:
        raise ZeroDivisionError("division by zero")


