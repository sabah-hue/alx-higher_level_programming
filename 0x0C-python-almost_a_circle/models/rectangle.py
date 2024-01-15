#!/usr/bin/python3
""" rectangle model """


from models.base import Base


class Rectangle(Base):
    """ rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ constractor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ get property """
        return self.__width

    @property
    def height(self):
        """ get property """
        return self.__height

    @property
    def x(self):
        """ get property """
        return self.__x

    @property
    def y(self):
        """ get property """
        return self.__y

    @width.setter
    def width(self, value):
        """ set property """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ set property """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ set property """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ set property """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ calculate area """
        return self.__width * self.__height

    def display(self):
        """ display rectangle """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """ print string"""
        z = f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"
        return z

    def update(self, *args, **kwargs):
        """ get property from args """
        arr = ['id', 'width', 'height', 'x', 'y']
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, arr[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ dictionary """
        return ({'id': self.id, 'x': self.x, 'height': self.height,
                'width': self.width, 'y': self.y})
