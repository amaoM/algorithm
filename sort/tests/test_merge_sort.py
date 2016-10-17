# coding: utf-8

import unittest
import merge_sort
import random

class TestCountingSort(unittest.TestCase):

    def test_merge_sort_1(self):
        lst = [0, 21, 15, 10, 8, 5]
        exp = [0, 5, 8, 10, 15, 21]
        self.assertEqual(merge_sort.merge_sort(lst), exp)

    def test_merge_sort_2(self):
        lst = create_random_int_list(500, 1000)
        self.assertEqual(merge_sort.merge_sort(lst), sorted(lst))

    def test_merge_sort_3(self):
        lst = create_random_int_list(1000, 1000)
        self.assertEqual(merge_sort.merge_sort(lst), sorted(lst))

def create_random_int_list(l, k):
    return [random.randint(0, k) for _ in range(l)]
