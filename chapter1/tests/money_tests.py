#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from money import dollar

class MoneyTest(unittest.TestCase):
    def test_multiplication(self):
        five = dollar.Dollar(5)
        five.times(2)
        self.assertEqual(10, five.amount)
