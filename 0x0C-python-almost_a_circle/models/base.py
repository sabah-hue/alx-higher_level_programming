#!/usr/bin/python3
""" module ... """

import json
from os import path


class Base:
    """class base """

    __nb_objects = 0

    def __init__(self, id=None):
        """ constractor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ json formate """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save file """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                json.dump([], f)
            else:
                newlist = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(newlist))

    @staticmethod
    def from_json_string(json_string):
        """ json string """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create dic """
        if cls.__name__ == "Rectangle":
            d = cls(1, 1)
        if cls.__name__ == "Square":
            d = cls(1)
        d.update(**dictionary)
        return d

    def load_from_file(cls):
        """load file """
        filename = cls.__name__ + ".json"
        z = []
        if os.path.exists(filename) is False:
            return []
        else:
            with open(filename, "r") as f:
                mylist = cls.from_json_string(f.read())
            for i in range(len(mylist)):
                z.append(cls.create(**mylist[i]))
            return z
