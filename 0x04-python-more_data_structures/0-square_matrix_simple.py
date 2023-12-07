#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [list(map(lambda r: r ** 2, row)) for row in matrix]
    return new_matrix
