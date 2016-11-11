#!/usr/bin/python
# -*- coding: utf-8 -*-
import math;

def factorial (n):
    if (n < 0):
        return -1
    wyn = 1
    for i in range (2,n+1):
        wyn *= i
    return wyn
        
print (factorial (10))
