#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractclassmethod

class Expression(metaclass=ABCMeta):

    @abstractclassmethod
    def reduce(self, bank, to):
        pass

    @abstractclassmethod
    def plus(self, addend):
        pass










