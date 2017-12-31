#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .money import Money
from .sum import Sum

class Bank:
    def reduce(self, source, to):
        return source.reduce(to)

    def addRate(self, source, to, rate):
        return None









