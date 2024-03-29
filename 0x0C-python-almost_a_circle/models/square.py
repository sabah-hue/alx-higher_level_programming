#!/usr/bin/python3
""" square model ... """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ constractor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ property size """
        return self.width

    @size.setter
    def size(self, value):
        """ set property """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """ print string """
        z = f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
        return z

    def update(self, *args, **kwargs):
        """ update function """
        arr = ['id', 'size', 'x', 'y']
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, arr[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ dic ... """
        return ({'id': self.id, 'x': self.x,
                'size': self.width, 'y': self.y})
