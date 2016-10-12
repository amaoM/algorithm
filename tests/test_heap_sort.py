# coding: utf-8

import unittest
import heap_sort
import random

class TestHeapSort(unittest.TestCase):

    def test_heap_sort_1(self):
        lst = [21, 15, 10, 8, 5]
        exp = [5, 8, 10, 15, 21]
        self.assertEqual(heap_sort.heap_sort(lst), exp)

    def test_heap_sort_2(self):
        lst = [8, 5, 4, 3, 2, 3, 0, 1, 3, 2]
        exp = [0, 1, 2, 2, 3, 3, 3, 4, 5, 8]
        self.assertEqual(heap_sort.heap_sort(lst), exp)

    def test_heap_sort_3(self):
        lst = [84, 69, 61, 63, 48, 23, 51, 44, 52, 37, 23, 7, 5, 24, 18, 32, 8, 17, 48, 36]
        exp = [5, 7, 8, 17, 18, 23, 23, 24, 32, 36, 37, 44, 48, 48, 51, 52, 61, 63, 69, 84]
        self.assertEqual(heap_sort.heap_sort(lst), exp)

    def test_heap_sort_4(self):
        lst = [216, 435, 238, 766, 116, 225, 243, 637, 479, 983, 851, 846, 906, 629, 120, 960, 573, 381,
            361, 949, 599, 168, 997, 487, 669, 565, 667, 635, 27, 269, 642, 81, 14, 988, 108, 418, 625,
            821, 166, 592, 530, 686, 850, 664, 719, 465, 236, 709, 510, 449, 971, 664, 994, 670, 410, 550,
            501, 61, 37, 810, 332, 324, 39, 30, 485, 318, 611, 546, 398, 852, 71, 904, 887, 540, 402, 985,
            265, 859, 76, 265, 772, 592, 819, 859, 359, 140, 990, 217, 850, 11, 198, 807, 780, 488, 410,
            328, 521, 697, 364, 778
        ]
        self.assertEqual(heap_sort.heap_sort(lst), sorted(lst))

    def test_heap_sort_4(self):
        lst = create_random_int_list(500, 1000)
        self.assertEqual(heap_sort.heap_sort(lst), sorted(lst))

    def test_heap_sort_5(self):
        lst = create_random_int_list(1000, 10)
        self.assertEqual(heap_sort.heap_sort(lst), sorted(lst))

def create_random_int_list(l, k):
    return [random.randint(0, k) for _ in range(l)]
