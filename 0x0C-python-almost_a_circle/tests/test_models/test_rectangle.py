#!/usr/bin/python3
"""This holds the unittest for class Rectangle"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests the Rectangle class"""
    def test_id(self):
        """Test One"""
        my_rect_1 = Rectangle(10, 2, 0, 0, 5)
        self.assertEqual(my_rect_1.id, 5)

    def test_validator(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle("10", 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r2 = Rectangle(0, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r3 = Rectangle(-1, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r4 = Rectangle(1, "2")
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r5 = Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r6 = Rectangle(1, -3)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r7 = Rectangle(1, 2, "1")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r8 = Rectangle(1, 2, -1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r9 = Rectangle(1, 2, 3, "1")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r10 = Rectangle(1, 2, 3, -1)
        c = Rectangle(1, 2, 3, 4)
        c.x = 0
        self.assertEqual(c.x, 0)
        c.y = 0
        self.assertEqual(c.y, 0)
