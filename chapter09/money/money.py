#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Money(metaclass=ABCMeta):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency 

    def __eq__(self, other):
        return (self._amount == other._amount) and \
            (self.__class__.__name__ == other.__class__.__name__)

    @abstractmethod
    def times(self, multiplier):
        pass

    def currency(self):
        return self._currency

    @staticmethod
    def dollar(amount):
        from .dollar import Dollar
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount):
        from .franc import Franc
        return Franc(amount, "CHF")
    
