#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .money import Money
from .sum import Sum

class Bank:
    def __init__(self):
        self._rates = {}
        
    def reduce(self, source, to):
        return source.reduce(self, to)

    def addRate(self, source, to, rate):
        self._rates[(source, to)] = rate

    def rate(self, source, to):
        if source == to:
            return 1  # identity
        return self._rates[(source, to)]

