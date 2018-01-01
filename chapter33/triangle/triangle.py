#!/usr/bin/env python
# -*- coding: utf-8 -*-


def triangleness(sides):
    if contains_negatives(sides):
        raise Exception
    
    sorted_sides = sorted(sides)
    max_side = sorted_sides.pop()
    rest_sides = sorted_sides
    if max_side >= sum(rest_sides):
        raise Exception
    return len(set(sides))

def contains_negatives(ls):
    for e in ls:
        if e <= 0:
            return True
        else:
            continue
    return False










