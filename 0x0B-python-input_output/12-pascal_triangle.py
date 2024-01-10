#!/usr/bin/python3
""" module ... """



def pascal_triangle(n):
    """ Pascal's Triangle """
    my_list = []
    if n <= 0:
        return my_list
    if n == 1:
        return [[1]]
    triangle = [[1]]
    for i in range(2, n+1):
        row = [1]
    return triangle
