#!/usr/bin/python3
""" module ... """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Improve Geometry """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        x = ("[{}] {}/{}".format
        (self.__class__.__name__, self.__width, self.__height))
        return x
