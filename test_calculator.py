"""
Test cases for the calculator module.
"""

import unittest
from calculator import add, subtract, multiply, divide, integer_divide, modulo


class TestCalculator(unittest.TestCase):

    def test_add(self):
        """Test addition function."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 5), 4)
        self.assertEqual(add(10, -7), 3)
        self.assertEqual(add(0, 8), 8)
        self.assertEqual(add(-3, -4), -7)

    def test_subtract(self):
        """Test subtraction function."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(10, 7), 3)
        self.assertEqual(subtract(-1, 5), -6)
        self.assertEqual(subtract(0, 8), -8)
        self.assertEqual(subtract(-3, -4), 1)

    def test_multiply(self):
        """Test multiplication function."""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(10, -7), -70)
        self.assertEqual(multiply(0, 8), 0)
        self.assertEqual(multiply(-3, -4), 12)

    def test_divide(self):
        """Test division function."""
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(15, 3), 5.0)
        self.assertEqual(divide(-8, 2), -4.0)
        self.assertEqual(divide(7, -1), -7.0)
        self.assertEqual(divide(-12, -3), 4.0)

    def test_divide_by_zero(self):
        """Test division by zero raises exception."""
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_integer_divide(self):
        """Test integer division function."""
        self.assertEqual(integer_divide(10, 3), 3)
        self.assertEqual(integer_divide(15, 4), 3)
        self.assertEqual(integer_divide(-8, 3), -3)
        self.assertEqual(integer_divide(7, -2), -4)
        self.assertEqual(integer_divide(-12, -5), 2)

    def test_integer_divide_by_zero(self):
        """Test integer division by zero raises exception."""
        with self.assertRaises(ZeroDivisionError):
            integer_divide(10, 0)

    def test_modulo(self):
        """Test modulo function."""
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(15, 4), 3)
        self.assertEqual(modulo(-8, 3), 1)
        self.assertEqual(modulo(7, -2), -1)
        self.assertEqual(modulo(-12, -5), -2)

    def test_modulo_by_zero(self):
        """Test modulo by zero raises exception."""
        with self.assertRaises(ZeroDivisionError):
            modulo(10, 0)


if __name__ == '__main__':
    # Run the tests
    unittest.main()