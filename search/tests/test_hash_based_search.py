# coding: utf-8

import unittest
import hash_based_search
import random

class TestCountingSort(unittest.TestCase):

    def test_hash_based_search_1(self):
        lst = [0, 21, 15, 10, 8, 5]
        exp = True
        self.assertEqual(hash_based_search.hash_based_search(21, 4, lst), exp)

    def test_hash_based_search_2(self):
        lst = create_random_int_list(500, 1000)
        exp = True
        self.assertEqual(hash_based_search.hash_based_search(lst[213], 7, lst), exp)

    def test_hash_based_search_3(self):
        lst = create_random_int_list(1000, 1000)
        exp = True
        self.assertEqual(hash_based_search.hash_based_search(lst[213], 9, lst), exp)

def create_random_int_list(l, k):
    return [random.randint(0, k) for _ in range(l)]
