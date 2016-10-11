# coding: utf-8

import unittest
import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_babble_sort(self):
        test_list = [5, 8, 10, 15, 21]
        self.assertEqual(binary_search.binary_search(8, test_list, 0, len(test_list) - 1), 1)
        self.assertEqual(binary_search.binary_search(21, test_list, 0, len(test_list) - 1), 4)
        self.assertEqual(binary_search.binary_search(10, test_list, 0, len(test_list) - 1), 2)
        test_list = [0, 1, 2, 2, 3, 3, 3, 4, 5, 8]
        self.assertEqual(binary_search.binary_search(3, test_list, 0, len(test_list) - 1), 4)
        self.assertEqual(binary_search.binary_search(4, test_list, 0, len(test_list) - 1), 7)
