#!/usr/bin/python3
"""Holds the unittest for class Square"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_init(self):
        """Tests __init__"""
        a = Square(5)
        self.assertEqual(a.width, 5)
        self.assertEqual(a.height, 5)
        self.assertEqual(a.x, 0)
        self.assertEqual(a.y, 0)
        self.assertEqual(a.area(), 25)

    def test_validator(self):
        """Tests validators in setters"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1 = Square("5")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s2 = Square(5.1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s3 = Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s4 = Square(-1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s5 = Square(1, "2")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s6 = Square(1, -1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s7 = Square(1, 2, "3")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s8 = Square(1, 2, -3)

    def test_update(self):
        """Tests the update instance method"""
        s = Square(5)
        args = (1,)
        s.update(*args)
        self.assertEqual(s.id, 1)
        s.update(id=2, size=6, x=2, y=3)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.width, 6)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
