# coding: utf-8

import unittest
import radix_sort

class TestRadixSort(unittest.TestCase):

    def test_radix_sort(self):
        test_list = [170, 45, 75, 90, 2, 24, 802, 66]
        self.assertEqual(radix_sort.radix_sort(test_list, 1), [2, 24, 45, 66, 75, 90, 170, 802])
