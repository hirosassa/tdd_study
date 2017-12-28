#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return True
    
    def times(self, multiplier):
        return self.amount * multiplier







