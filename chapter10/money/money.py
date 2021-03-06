#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Money(metaclass=ABCMeta):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency 

    def __str__(self):
        return str(self._amount) + " " + self._currency

    def __eq__(self, other):
        return (self._amount == other._amount) and \
            (self._currency == other._currency)

    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)

    def currency(self):
        return self._currency

    @staticmethod
    def dollar(amount):
        from .dollar import Dollar
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        from .franc import Franc
        return Money(amount, "CHF")
    
