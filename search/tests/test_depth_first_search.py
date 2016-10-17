# coding: utf-8

import unittest
import depth_first_search
import random

class TestDepthFirstSearch(unittest.TestCase):

    def test_depth_first_search_1(self):
        graph = [
            #s, 1, 2, 3, 4, 5, 6, 7, 8, 9, t
            [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0], #s
            [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], #1
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], #2
            [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], #3
            [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], #4
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0], #5
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], #6
            [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0], #7
            [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], #8
            [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1], #9
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]  #t
        ]
        exp = True
        self.assertEqual(depth_first_search.depth_first_search(graph), exp)
