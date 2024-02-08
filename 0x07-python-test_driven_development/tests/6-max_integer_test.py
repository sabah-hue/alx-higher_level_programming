#!/usr/bin/python3
""" unit test module """

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ test class for max integer """

    def test_single_element(self):
        """ test one element in list """
        self.assertEqual(max_integer([4], 4)

    def test_empty(self):
        """ test list is empty or no input passed """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

    def test_Normal_case(self):
        """ test in default case """
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_not_integer(self):
        """ test type error """
        with self.assertRaises(TypeError):
            max_integer([3, 2, "sabah", 5])

    def test_negative(self):
        """ test negative number """
        self.assertEqual(max_integer([1, -3, 3]), 3)

if __name__ == '__main__':
    unittest.main()
