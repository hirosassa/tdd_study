#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .money import Money


class Franc(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)
        
    def times(self, multiplier):
        return super().franc(self._amount * multiplier)
