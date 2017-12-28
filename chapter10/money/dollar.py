#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .money import Money


class Dollar(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)
