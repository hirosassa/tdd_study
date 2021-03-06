#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from money import dollar

class MoneyTest(unittest.TestCase):
    def test_multiplication(self):
        five = dollar.Dollar(5)
        product = five.times(2)
        self.assertEqual(10, product)
        product = five.times(3)
        self.assertEqual(15, product)
