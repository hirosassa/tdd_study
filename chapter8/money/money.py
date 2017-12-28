#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Money(metaclass=ABCMeta):
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return (self.amount == other.amount) and \
            (self.__class__.__name__ == other.__class__.__name__)

    @abstractmethod
    def times(self, multiplier):
        pass
    
    @staticmethod
    def dollar(amount):
        from .dollar import Dollar
        return Dollar(amount)

    @staticmethod
    def franc(amount):
        from .franc import Franc
        return Franc(amount)
    
