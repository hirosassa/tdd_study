#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .expression import Expression


class Money(Expression):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency 

    def __str__(self):
        return str(self._amount) + " " + self._currency

    def __eq__(self, other):
        return (self._amount == other._amount) and \
            (self._currency == other._currency)

    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)

    def amount(self):
        return self._amount

    def currency(self):
        return self._currency

    def plus(self, addend):
        from .sum import Sum
        return Sum(self, addend)

    def reduce(self, to):
        return self

    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")
    

