#!/usr/bin/python3
"""This holds the unittest for class Rectangle"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests the Rectangle class"""
    def test_rect_is_base(self):
        """Test One"""
        my_rect_1 = Rectangle(10, 2, 0, 0, 5)
        self.assertIsInstance(my_rect_1, Base)

    def test_no_params(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_param(self):
        with self.assertRaises(TypeError):
            Rectangle(5)

    def test_two_params(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(3, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_params(self):
        r1 = Rectangle(2, 3, 0)
        r2 = Rectangle(3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_params(self):
        r1 = Rectangle(2, 3, 0, 0)
        r2 = Rectangle(3, 2, 0, 0)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_params(self):
        r1 = Rectangle(2, 3, 0, 0, 5)
        r2 = Rectangle(3, 2, 0, 0, 12)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r2.id, 12)

    def test_six_params(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 10)

    def test_width_is_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(3, 2).__width)

    def test_height_is_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(3, 2).__height)

    def test_x_is_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(3, 2).__x)

    def test_y_is_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(3, 2).__y)

    def test_width_getter(self):
        self.assertEqual(Rectangle(3, 2).width, 3)

    def test_height_getter(self):
        self.assertEqual(Rectangle(3, 2).height, 2)

    def test_x_getter(self):
        self.assertEqual(Rectangle(3, 2).x, 0)

    def test_y_getter(self):
        self.assertEqual(Rectangle(3, 2).y, 0)

    def test_width_setter(self):
        r1 = Rectangle(3, 2)
        r1.width = 2
        self.assertEqual(r1.width, 2)

    def test_height_setter(self):
        r1 = Rectangle(3, 2)
        r1.height = 3
        self.assertEqual(r1.height, 3)

    def test_x_setter(self):
        r1 = Rectangle(3, 2)
        r1.x = 2
        self.assertEqual(r1.x, 2)

    def test_y_setter(self):
        r1 = Rectangle(3, 2)
        r1.y = 2
        self.assertEqual(r1.y, 2)


class TestRectangle_width(unittest.TestCase):
    """Test validates the width attribute"""
    def test_width_is_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_width_is_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("3", 2)

    def test_width_is_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(3.0, 2)

    def test_width_is_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_width_is_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"One": 3}, 2)

    def test_width_is_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 2)

    def test_width_is_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 2)

    def test_width_is_range(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(0, 3), 2)

    def test_width_is_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((3, ), 2)

    def test_width_is_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 2)

    def test_width_is_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(False, 2)

    def test_width_is_complex(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(3), 2)

    def test_width_is_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-3, 2)

    def test_width_is_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)


class TestRectangle_height(unittest.TestCase):
    """Test validates the height attribute"""
    def test_height_is_none(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, None)

    def test_height_is_str(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, "2")

    def test_height_is_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, 2.0)

    def test_height_is_list(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, [1, 2])

    def test_height_is_dict(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, {"one": 2})

    def test_height_is_inf(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, float('inf'))

    def test_height_is_nan(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, float('nan'))

    def test_height_is_range(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, range(0, 2))

    def test_height_is_tuple(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, (2, ))

    def test_height_is_set(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, {1, 2})

    def test_height_is_bool(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, False)

    def test_height_is_complex(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, complex(2))

    def test_height_is_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, -2)

    def test_height_is_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, 0)


class TestRectangle_x(unittest.TestCase):
    """Test validates the x attribute"""
    def test_x_is_none(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 2, None, 0)

    def test_x_is_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 2, "0", 0)

    def test_x_is_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 2, 0.1, 0)

    def test_x_is_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 2, [1, 2], 0)

    def test_x_is_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 2, {"one": 2}, 0)

    def test_x_is_inf(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 2, float('inf'), 0)

    def test_x_is_nan(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 2, float('nan'), 0)

    def test_x_is_range(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 2, range(0, 3), 0)

    def test_x_is_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 2, (0, ), 0)

    def test_x_is_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 2, {1, 2}, 0)

    def test_x_is_bool(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 2, False, 0)

    def test_x_is_complex(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 2, complex(2), 0)

    def test_x_is_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(3, 2, -1, 0)


class TestRectangle_y(unittest.TestCase):
    """Test validates the y attribute"""
    def test_y_is_none(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 2, 0, None)

    def test_y_is_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 2, 0, "0")

    def test_y_is_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 2, 0, 0.1)

    def test_y_is_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 2, 0, [1, 2])

    def test_y_is_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 2, 0, {"one": 2})

    def test_y_is_inf(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 2, 0, float('inf'))

    def test_y_is_nan(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 2, 0, float('nan'))

    def test_y_is_range(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 2, 0, range(0, 3))

    def test_y_is_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 2, 0, (0,))

    def test_y_is_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 2, 0, {1, 2})

    def test_y_is_bool(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 2, 0, False)

    def test_y_is_complex(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 2, 0, complex(2))

    def test_y_is_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 2, 0, -1)
