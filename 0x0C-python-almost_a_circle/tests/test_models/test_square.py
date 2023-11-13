#!/usr/bin/python3
"""This holds the unittest for class Square"""
import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests the Square class"""
    def test_square_is_rectangle(self):
        """Test One"""
        s1 = Square(10, 2, 0, 5)
        self.assertIsInstance(s1, Rectangle)

    def test_no_params(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_param(self):
        sq = Square(5)
        sq1 = Square(3)
        self.assertEqual(sq.id, sq1.id - 1)

    def test_two_params(self):
        s1 = Square(2, 3)
        s2 = Square(3, 2)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_params(self):
        s1 = Square(2, 3, 0)
        s2 = Square(3, 2, 1)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_params(self):
        s1 = Square(2, 3, 0, 5)
        s2 = Square(3, 2, 0, 12)
        self.assertEqual(s1.id, 5)
        self.assertEqual(s2.id, 12)

    def test_five_params(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_is_private(self):
        with self.assertRaises(AttributeError):
            print(Square(3).__size)

    def test_size_getter(self):
        self.assertEqual(Square(3).size, 3)

    def test_width_getter(self):
        self.assertEqual(Square(3).width, 3)

    def test_height_getter(self):
        self.assertEqual(Square(3).height, 3)

    def test_x_getter(self):
        self.assertEqual(Square(3, 2).x, 2)

    def test_y_getter(self):
        self.assertEqual(Square(3, 2).y, 0)

    def test_size_setter(self):
        s1 = Square(3)
        s1.size = 5
        self.assertEqual(s1.size, 5)

    def test_width_setter(self):
        s1 = Square(3, 2)
        s1.size = 2
        self.assertEqual(s1.width, 2)

    def test_height_setter(self):
        s1 = Square(3, 2)
        s1.height = 4
        self.assertEqual(s1.height, 4)

    def test_x_setter(self):
        s1 = Square(3, 2)
        s1.x = 1
        self.assertEqual(s1.x, 1)

    def test_y_setter(self):
        s1 = Square(3, 2)
        s1.y = 2
        self.assertEqual(s1.y, 2)


class TestSquare_size(unittest.TestCase):
    """Test validates the width attribute"""
    def test_size_is_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None, 2)

    def test_size_is_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("3", 2)

    def test_size_is_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(3.0, 2)

    def test_size_is_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3], 2)

    def test_size_is_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"One": 3}, 2)

    def test_size_is_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'), 2)

    def test_size_is_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'), 2)

    def test_size_is_range(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(0, 3), 2)

    def test_size_is_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((3, ), 2)

    def test_size_is_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3}, 2)

    def test_size_is_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(False, 2)

    def test_size_is_complex(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(3), 2)

    def test_size_is_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-3, 2)

    def test_size_is_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)


class TestSquare_x(unittest.TestCase):
    """Test validates the x attribute"""
    def test_x_is_none(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, None, 0)

    def test_x_is_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, "0", 0)

    def test_x_is_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, 0.1, 0)

    def test_x_is_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, [1, 2], 0)

    def test_x_is_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, {"one": 2}, 0)

    def test_x_is_inf(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, float('inf'), 0)

    def test_x_is_nan(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, float('nan'), 0)

    def test_x_is_range(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, range(0, 3), 0)

    def test_x_is_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, (0, ), 0)

    def test_x_is_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, {1, 2}, 0)

    def test_x_is_bool(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, False, 0)

    def test_x_is_complex(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, complex(2), 0)

    def test_x_is_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(3, -1, 0)


class TestSquare_y(unittest.TestCase):
    """Test validates the y attribute"""
    def test_y_is_none(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 0, None)

    def test_y_is_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 0, "0")

    def test_y_is_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 0, 0.1)

    def test_y_is_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 0, [1, 2])

    def test_y_is_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 0, {"one": 2})

    def test_y_is_inf(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 0, float('inf'))

    def test_y_is_nan(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 0, float('nan'))

    def test_y_is_range(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 0, range(0, 3))

    def test_y_is_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 0, (0,))

    def test_y_is_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 0, {1, 2})

    def test_y_is_bool(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 0, False)

    def test_y_is_complex(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 0, complex(2))

    def test_y_is_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 0, -1)
