#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Franc:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount
    
    def times(self, multiplier):
        return Franc(self.amount * multiplier)










