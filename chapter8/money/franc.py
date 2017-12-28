#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .money import Money


class Franc(Money):    
    def times(self, multiplier):
        return Franc(self.amount * multiplier)

