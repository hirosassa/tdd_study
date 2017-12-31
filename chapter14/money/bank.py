#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .money import Money
from .sum import Sum

class Bank:
    def reduce(self, source, to):
        return source.reduce(self, to)

    def addRate(self, source, to, rate):
        return None

    def rate(self, source, to):
        return 2 if (source == "CHF") and (to == "USD") else 1
