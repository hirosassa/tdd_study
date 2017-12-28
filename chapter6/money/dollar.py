#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .money import Money


class Dollar(Money):    
    def times(self, multiplier):
        return Dollar(self.amount * multiplier)
