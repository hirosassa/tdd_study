#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from triangle import triangle

class TriangleTest(unittest.TestCase):
    def test_not_triangle(self):
        sides = [1, 5, 2]
        with self.assertRaises(Exception):
            triangle.triangleness(sides)

    def test_regular_triangle(self):
        sides = [2, 2, 2]
        self.assertEqual(1, triangle.triangleness(sides))

    def test_isosceles_triangle(self):
        sides = [5, 5, 3]
        self.assertEqual(2, triangle.triangleness(sides))

    def test_scalene_triangle(self):
        sides = [4, 6, 3]
        self.assertEqual(3, triangle.triangleness(sides))
        
