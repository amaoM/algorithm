# coding: utf-8

import unittest
import quick_sort

class TestBabbleSort(unittest.TestCase):

    def test_babble_sort(self):
        test_list = [10, 8, 15, 21, 5]
        self.assertEqual(quick_sort.quick_sort([10, 8, 15, 21, 5], 0, len(test_list) - 1), [5, 8, 10, 15, 21])
        test_list = [3, 2, 0, 5, 8, 3, 4, 1, 3, 2]
        self.assertEqual(quick_sort.quick_sort([3, 2, 0, 5, 8, 3, 4, 1, 3, 2], 0, len(test_list) - 1), [0, 1, 2, 2, 3, 3, 3, 4, 5, 8])
        test_list = [48, 44, 7, 63, 37, 24, 18, 69, 48, 84, 23, 23, 5, 51, 61, 32, 8, 17, 52, 36]
        self.assertEqual(quick_sort.quick_sort([48, 44, 7, 63, 37, 24, 18, 69, 48, 84, 23, 23, 5, 51, 61, 32, 8, 17, 52, 36], 0, len(test_list) - 1), [5, 7, 8, 17, 18, 23, 23, 24, 32, 36, 37, 44, 48, 48, 51, 52, 61, 63, 69, 84])
