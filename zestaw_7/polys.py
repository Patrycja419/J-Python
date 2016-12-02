#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import sqrt

class Poly:
    """Klasa reprezentująca wielomiany."""

    # wg Sedgewicka - tworzymy wielomian c*x^n
    def __init__(self, c=0, n=0):
        self.size = n + 1       # rozmiar tablicy
        self.a = self.size * [0]
        self.a[self.size-1] = c

    def __str__(self):
        return str(self.a)

    def __add__(self, other):   # poly1 + poly2
        return Poly(self.poly1 + other.poly2)

    def __sub__(self, other):   # poly1 - poly2
        return Poly(self.poly1 - other.poly2)

    def __mul__(self, other):   # poly1 * poly2
        return Poly(self.poly1 * other.poly2)

    def __pos__(self): pass         # +poly1 = (+1)*poly1
    if self.(+poly1)==self.(+1)*poly1
            return True
        else:
            return False
    def __neg__(self): # -poly1 = (-1)*poly1
    if self.(-poly1)==self.(-1)*poly1
            return True
        else:
            return False
    def __eq__(self, other):   # obsługa poly1 == poly2 
    sub = self-other
        if sub.x == 0: # self = other
            return True
        else:
            return False
    
    def __ne__(self, other):        # obsługa poly1 != poly2
        return not self == other

    def eval(self, x): pass         # schemat Hornera

    def combine(self, other):       # złożenie poly1(poly2(x))

    def __pow__(self, n): pass      # poly(x)**n lub pow(poly(x),n)

    def diff(self):             # różniczkowanie
    return Poly(self.(a+n) - self.(n))/a
    
    def integrate(self): pass       # całkowanie

    def is_zero(self): pass         # bool, True dla [0], [0, 0],...
