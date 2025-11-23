import unittest
from src.sorts import (
    bubble_sort, quick_sort, merge_sort, heap_sort,
    count_sort, radix_sort, bucket_sort
)



class TestSorting(unittest.TestCase):

    def setUp(self):
        self.base = [5, 1, 4, 2, 8]

    def check_sorted(self, func, arr):
        self.assertEqual(func(arr.copy()), sorted(arr))

    def test_basic_sorting(self):
        for sort in [bubble_sort, quick_sort, merge_sort, heap_sort]:
            with self.subTest(sort=sort.__name__):
                self.check_sorted(sort, self.base)

    def test_count_sort(self):
        self.assertEqual(count_sort(self.base.copy()), sorted(self.base))

    def test_radix_sort(self):
        self.assertEqual(radix_sort(self.base.copy()), sorted(self.base))

    def test_bucket_sort(self):
        arr = [0.2, 0.9, 0.4, 0.1]
        self.assertEqual(bucket_sort(arr.copy()), sorted(arr))

    def test_key(self):
        arr = [-5, 2, -1, 3]
        res = quick_sort(arr.copy(), key=lambda x: abs(x))
        self.assertEqual(res, [-1, 2, 3, -5])

    def test_comparator(self):
        def reverse(a, b): return b - a
        arr = [1, 2, 3]
        res = merge_sort(arr.copy(), cmp=reverse)
        self.assertEqual(res, [3, 2, 1])

    def test_key_not_supported(self):
        with self.assertRaises(TypeError):
            count_sort([1, 2, 3], key=lambda x: x)

    def test_cmp_not_supported(self):
        with self.assertRaises(TypeError):
            radix_sort([1, 2, 3], cmp=lambda a, b: a - b)
