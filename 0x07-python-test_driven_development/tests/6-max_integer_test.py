#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Inherits from Testcases"""

    def test_empty(self):
        """Tests empty list"""
        self.assertIsNone(max_integer())

    def test_all_int(self):
        """Tests a unsorted all integer list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-3, -1, -10, -20]), -1)
        self.assertEqual(max_integer([[2, 4], [0, 1], [3, -1]]), [3, -1])
        self.assertEqual(max_integer((1, 2, 4, 6, 100)), 100)
        self.assertEqual(max_integer([8, 2, 1]), 8)
        self.assertEqual(max_integer([8]), 8)

    def test_all_str(self):
        """Tests an all string integer"""
        self.assertEqual(max_integer(["Jane", "June", "July", "Jade"]), "June")

    def test_all_float(self):
        self.assertEqual(max_integer([-1.2, -10.7, 0.8, 0000.8]), 0.8)
        self.assertEqual(max_integer([[-10.7, 1.3], [-30.2, 0.1], [0.1, -40.8]]), [0.1, -40.8])

    def test_type(self):
       self.assertRaises(TypeError, max_integer, ['a', 2])
       self.assertRaises(KeyError, max_integer, {"seth": 5, "joshua": 10})
