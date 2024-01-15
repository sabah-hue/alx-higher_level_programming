#!/usr/bin/python3
""" square model ... """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ constractor """
        super().__init__(size, size, x, y, id)
        self.size = size
        self.x = x
        self.y = y
        self.id = id

    @property
    def size(self):
        """ property size """
        return self.width

    @size.setter
    def size(self, value):
        """ set property """
        self.width = value
        self.height = value

    def __str__(self):
        """ print string """
        z = f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
        return z
