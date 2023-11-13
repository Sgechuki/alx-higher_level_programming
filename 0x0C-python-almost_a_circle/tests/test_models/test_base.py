#!/usr/bin/python3
"""This is a unittest for class Base"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests class Base"""

    def test_id(self):
        """when id is assigned"""
        my_base = Base(1)
        self.assertEqual(my_base.id, 1)

    def test_id_default(self):
        """default id when not assigned"""
        my_base = Base()
        my_base_1 = Base()
        self.assertEqual(my_base.id, my_base_1.id - 1)

    def test_id_nb_object(self):
        """test nb_object increment"""
        my_base = Base()
        my_base_1 = Base()
        my_base_2 = Base()
        self.assertEqual(my_base.id, my_base_1.id - 1)
        self.assertEqual(my_base_1.id, my_base_2.id - 1)

    def test_id_alt(self):
        """test case when id is assigned and not assigned"""
        my_base = Base(5)
        my_base_1 = Base()
        my_base_2 = Base(1738)
        my_base_3 = Base()
        self.assertEqual(my_base.id, 5)
        self.assertEqual(my_base_1.id, my_base_3.id - 1)
        self.assertEqual(my_base_2.id, 1738)
