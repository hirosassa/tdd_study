#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from money.money import Money
from money.bank import Bank
from money.sum import Sum

class MoneyTest(unittest.TestCase):
    def test_multiplication(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five.times(2))
        self.assertEqual(Money.dollar(15), five.times(3))

    def test_equality(self):
        self.assertTrue(Money.dollar(5) == Money.dollar(5))
        self.assertFalse(Money.dollar(5) == Money.dollar(6))
        self.assertFalse(Money.franc(5) == Money.dollar(5))

    def test_currency(self):
        self.assertEqual("USD", Money.dollar(1).currency())
        self.assertEqual("CHF", Money.franc(1).currency())

    def test_simple_addtion(self):
        five = Money.dollar(5)
        sum = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(sum, "USD")
        self.assertEqual(Money.dollar(10), reduced)

    def test_plus_return_sum(self):
        five = Money.dollar(5)
        result = five.plus(five)
        sum = result
        self.assertEqual(five, sum.augend())
        self.assertEqual(five, sum.addend())

    def test_reduce_sum(self):
        sum = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(sum, "USD")
        self.assertEqual(Money.dollar(7), result)

    def test_reduce_money(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1), "USD")
        self.assertEqual(Money.dollar(1), result)

    def test_reduce_money_different_currency(self):
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        result = bank.reduce(Money.franc(2), "USD")
        self.assertEqual(Money.dollar(1), result)
        
    def test_identity_rate(self):
        self.assertEqual(1, Bank().rate("USD", "USD"))

    def test_mixed_addtion(self):
        five_dollars = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        result = bank.reduce(five_dollars.plus(ten_francs), "USD")
        self.assertEqual(Money.dollar(10), result)

    def test_sum_plus_money(self):
        five_dollars = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        sum = Sum(five_dollars, ten_francs).plus(five_dollars)
        result = bank.reduce(sum, "USD")
        self.assertEqual(Money.dollar(15), result)

    def test_sum_times(self):
        five_dollars = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        sum = Sum(five_dollars, ten_francs).times(2)
        result = bank.reduce(sum, "USD")
        self.assertEqual(Money.dollar(20), result)
