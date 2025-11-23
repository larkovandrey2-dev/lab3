import unittest
from src.addons.tests_generator import (
    rand_int_array, nearly_sorted,
    many_duplicates, reverse_sorted,
    rand_float_array
)


class TestGenerators(unittest.TestCase):

    def test_rand_int_basic(self):
        arr = rand_int_array(5, 0, 10, seed=1)
        self.assertEqual(len(arr), 5)

    def test_rand_int_distinct(self):
        arr = rand_int_array(5, 0, 100, distinct=True, seed=1)
        self.assertEqual(len(arr), len(set(arr)))

    def test_nearly_sorted(self):
        arr = nearly_sorted(10, 2, seed=1)
        self.assertEqual(len(arr), 10)

    def test_many_duplicates(self):
        arr = many_duplicates(100, k_unique=3, seed=1)
        self.assertLessEqual(len(set(arr)), 3)

    def test_reverse_sorted(self):
        self.assertEqual(reverse_sorted(5), [5,4,3,2,1])

    def test_rand_float(self):
        arr = rand_float_array(5, 0.0, 1.0, seed=1)
        self.assertEqual(len(arr), 5)
        self.assertTrue(all(0 <= x <= 1 for x in arr))
