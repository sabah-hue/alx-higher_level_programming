#!/usr/bin/python3
""" model test """


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
import sys
import json


class test_square(unittest.TestCase):
    """class test """
     def tearDown(self):
         """ erease ... """
         pass
