#!/usr/bin/python
# -*- coding: utf-8 -*-
import math;

def sum_seq(sequence):
    suma = 0
    for i in range(len(sequence)):
        if isinstance(sequence[i], (list,tuple)):
            suma += sum_seq(sequence[i])
        else:
            suma += sequence[i]
    return suma

seq = [1,(6,3),[5,6],[4,(5,6,7)],8]
print(sum_seq(seq))

