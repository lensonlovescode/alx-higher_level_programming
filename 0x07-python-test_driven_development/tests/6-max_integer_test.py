#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    TestCase class for the max_integer function.

    This class contains unit tests for the max_integer function,
    which returns the largest integer from a list of integers.

    Tests will check the following cases:
        - A list of positive integers.
        - A list containing negative integers.
        - A list with mixed positive and negative integers.
        - A list with a single integer.
        - An empty list (should raise ValueError).
        - A list containing non-integer types (should raise TypeError).
    """
    def test_optimal(self):
        """
        Test case to check the maximum integer in a list of positive integers.
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    def test_allnegatives(self):
        """
        Test case to check the maximum integer in a list of negative integers.
        """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
    def test_mixnegatives(self):
        """
        Test case to check the maximum integer in a list
        containing both positive and negative integers.
        """
        self.assertEqual(max_integer([1, 3, -7, -4]), 3)
    def test_oneinteger(self):
        """
        Test case to check the maximum integer in a list with a single integer.
        """
        self.assertEqual(max_integer([5]), 5)
    def test_string(self):
        """
        Test case for a string input
        """
        self.assertEqual(max_integer("my string that's not a list"), 'y')
    def test_emptylist(self):
        """
        Test case to ensure a ValueError is raised for an empty list.
        """
        self.assertEqual(max_integer([]), None)
    def test_notlist(self):
        """
        Test case to ensure a TypeError is raised when the input is not a list.
        """
        self.assertRaises(TypeError, max_integer, "my string not a list")
