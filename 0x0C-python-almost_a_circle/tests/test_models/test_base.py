#!/usr/bin/python3
"""This is a unittest for class Base"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests class Base"""

    def test_attr_id(self):
        """when id is None"""
        my_base_1 = Base()
        self.assertEqual(my_base_1.id, 1)
        my_base_2 = Base()
        self.assertEqual(my_base_2.id, 2)
        my_base_3 = Base()
        self.assertEqual(my_base_3.id, 3)
        """when id is not None"""
        my_base_4 = Base(5)
        self.assertEqual(my_base_4.id, 5)
        my_base_5 = Base()
        self.assertEqual(my_base_5.id, 4)
