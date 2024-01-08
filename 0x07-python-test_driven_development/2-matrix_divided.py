#!/usr/bin/python3
""" module """


def matrix_divided(matrix, div):
    """ division """
    x = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(x)

    div_matrix = []
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        if type(row) is not list or len(row) == 0:
            raise TypeError(x)
        div_row = []
        for e in row:
            if type(e) is int or type(e) is float:
                div_row.append(round(e / div, 2))
            else:
                raise TypeError(x)
        div_matrix.append(div_row)

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    return div_matrix
