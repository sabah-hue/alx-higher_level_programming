#!/usr/bin/python3
""" square model ... """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size
        self.x = x
        self.y = y
        self.id = id

    def __str__(self):
        z = f"[Square] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"
        return z

