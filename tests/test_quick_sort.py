# coding: utf-8

import unittest
import quick_sort
import random

class TestBabbleSort(unittest.TestCase):

    def test_babble_sort_1(self):
        lst = [10, 8, 15, 21, 5]
        exp = sorted(lst)
        self.assertEqual(quick_sort.quick_sort(lst, 0, len(lst) - 1), exp)

    def test_babble_sort_2(self):
        lst = [3, 2, 0, 5, 8, 3, 4, 1, 3, 2]
        exp = sorted(lst)
        self.assertEqual(quick_sort.quick_sort(lst, 0, len(lst) - 1), exp)

    def test_babble_sort_3(self):
        lst = [48, 44, 7, 63, 37, 24, 18, 69, 48, 84, 23, 23, 5, 51, 61, 32, 8, 17, 52, 36]
        exp = sorted(lst)
        self.assertEqual(quick_sort.quick_sort(lst, 0, len(lst) - 1), exp)

    def test_babble_sort_4(self):
        lst = create_random_int_list(10000, 1000)
        exp = sorted(lst)
        self.assertEqual(quick_sort.quick_sort(lst, 0, len(lst) - 1), exp)

def create_random_int_list(l, k):
    return [random.randint(0, k) for _ in range(l)]
