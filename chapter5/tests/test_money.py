#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from money import dollar, franc

class MoneyTest(unittest.TestCase):
    def test_multiplication(self):
        five = dollar.Dollar(5)
        self.assertEqual(dollar.Dollar(10), five.times(2))
        self.assertEqual(dollar.Dollar(15), five.times(3))

    def test_equality(self):
        self.assertTrue(dollar.Dollar(5) == dollar.Dollar(5))
        self.assertFalse(dollar.Dollar(5) == dollar.Dollar(6))

    def test_franc_multiplication(self):
        five = fran.Fran(5)
        self.assertEqual(fran.Fran(10), five.times(2))
        self.assertEqual(fran.Fran(15), five.times(3))
