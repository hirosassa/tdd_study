#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return (self.amount == other.amount) and \
            (self.__class__.__name__ == other.__class__.__name__)
    
    
