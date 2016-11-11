#!/usr/bin/python
# -*- coding: utf-8 -*-
import math;

def flatten(sequence):
    newList = list()
    for i in range(len(sequence)):
        if isinstance(sequence[i], (list,tuple)):
            newList.extend(flatten(sequence[i]))
        else:
            newList.append(sequence[i])
    return newList

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(flatten(seq))

