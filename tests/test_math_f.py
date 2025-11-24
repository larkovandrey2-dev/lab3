import unittest
from src.fact_fib import factorial_recursive,factorial_iterative,fib_iterative,fib_recursive

class TestMathFunctions(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial_recursive(1), 1)
        self.assertEqual(factorial_iterative(1), 1)
        self.assertEqual(factorial_iterative(5),120)
        self.assertEqual(factorial_recursive(5),120)
    def test_big_factorial(self):
        self.assertRaises(ValueError, factorial_recursive, 1000)
        self.assertRaises(ValueError, factorial_recursive, 5000)
    def test_fib(self):
        self.assertEqual(fib_recursive(20), 10946)
        self.assertEqual(fib_iterative(20), 10946)
        self.assertEqual(fib_iterative(11),144)
        self.assertEqual(fib_recursive(11),144)
    def test_big_fib(self):
        self.assertRaises(ValueError, fib_recursive, 100)
        self.assertRaises(ValueError, fib_recursive, 60)
