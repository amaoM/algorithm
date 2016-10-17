# coding: utf-8

import unittest
import babble_sort
import heap_sort
import quick_sort
import random
import time
import inspect

class TestSortAlgorithm(unittest.TestCase):
    start = 0
    case_name = ''

    def setUp(self):
        self.start = time.time()

    def tearDown(self):
        print('{}: {}'.format(self.case_name, time.time() - self.start))

    def test_babble_sort_1(self):
        self.case_name = inspect.currentframe().f_code.co_name
        lst = create_random_int_list(1000, 10)
        exp = sorted(lst)
        self.assertEqual(babble_sort.babble_sort(lst), exp)

    def test_babble_sort_2(self):
        self.case_name = inspect.currentframe().f_code.co_name
        lst = create_random_int_list(10000, 10)
        exp = sorted(lst)
        self.assertEqual(babble_sort.babble_sort(lst), exp)

    def test_quick_sort_1(self):
        self.case_name = inspect.currentframe().f_code.co_name
        lst = create_random_int_list(1000, 10)
        exp = sorted(lst)
        self.assertEqual(quick_sort.quick_sort(lst, 0, len(lst) - 1), exp)

    def test_quick_sort_2(self):
        self.case_name = inspect.currentframe().f_code.co_name
        lst = create_random_int_list(10000, 10)
        exp = sorted(lst)
        self.assertEqual(quick_sort.quick_sort(lst, 0, len(lst) - 1), exp)

    def test_heap_sort_1(self):
        self.case_name = inspect.currentframe().f_code.co_name
        lst = create_random_int_list(1000, 10)
        exp = sorted(lst)
        self.assertEqual(heap_sort.heap_sort(lst), exp)

    def test_heap_sort_2(self):
        self.case_name = inspect.currentframe().f_code.co_name
        lst = create_random_int_list(10000, 10)
        exp = sorted(lst)
        self.assertEqual(heap_sort.heap_sort(lst), exp)

def create_random_int_list(l, k):
    return [random.randint(0, k) for _ in range(l)]
