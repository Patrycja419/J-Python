#!/usr/bin/python
# -*- coding: utf-8 -*-
import math;

def odwracanie (L, left, right): # rekurencyjnie
    if(left >= right):
        return None
    L[left],L[right] = L[right],L[left]
    if(left+1 != right):
        odwracanie(L,left+1,right-1)
        
lista = list(range(20))
odwracanie(lista, 5,15)
print (lista)

def odwracanie (L, left, right): # iteracyjnie
    if(left >= right):
        return None
    for i in range(int((right-left)/2)):
        L[left+i],L[right-i] = L[right-i],L[left+i]
        
lista = list(range(20))
odwracanie(lista, 5,15)
print (lista)

