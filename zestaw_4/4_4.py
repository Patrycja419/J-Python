#!/usr/bin/python
# -*- coding: utf-8 -*-
import math;

def fibonacci(n):
    a,b = (0, 1)
    while n > 0:
        print b,
        a, b = b, a + b
        n -= 1

n = int(raw_input("Podaj numer wyrazu: "))
fibonacci(n)
print ""
