# coding: utf-8

import unittest
import babble_sort

class TestBabbleSort(unittest.TestCase):

    def test_babble_sort(self):
        self.assertEqual(babble_sort.babble_sort([10, 8, 15, 21, 5]), [5, 8, 10, 15, 21])
        self.assertEqual(babble_sort.babble_sort([3, 2, 0, 5, 8, 3, 4, 1, 3, 2]), [0, 1, 2, 2, 3, 3, 3, 4, 5, 8])
        self.assertEqual(babble_sort.babble_sort([48, 44, 7, 63, 37, 24, 18, 69, 48, 84, 23, 23, 5, 51, 61, 32, 8, 17, 52, 36]), [5, 7, 8, 17, 18, 23, 23, 24, 32, 36, 37, 44, 48, 48, 51, 52, 61, 63, 69, 84])
