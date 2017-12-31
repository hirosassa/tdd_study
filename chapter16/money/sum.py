#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .money import Expression
from .money import Money

class Sum(Expression):
    def __init__(self, augend, addend):
        self._augend = augend
        self._addend = addend

    def augend(self):
        return self._augend

    def addend(self):
        return self._addend

    def reduce(self, bank, to):
        amount = (self._augend.reduce(bank, to).amount() +
                  self._addend.reduce(bank, to).amount())
        return Money(amount, to)

    def plus(self, addend):
        return Sum(self, addend)

    def times(self, multiplier):
        return Sum(self.augend().times(multiplier) , self.addend().times(multiplier))










