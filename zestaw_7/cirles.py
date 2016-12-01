#!/usr/bin/python
# -*- coding: utf-8 -*-

from points import Point
from math import pi
class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x=0, y=0, radius=1):
        if not ((isinstance(x, float) or isinstance(x, int)) and (isinstance(y, float) or isinstance(y, int)) and (isinstance(radius, float) or isinstance(radius, int))):
            raise ValueError("niepoprawny typ argumentu")
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = float(radius)
    def __repr__(self):       # "Circle(x, y, radius)"
        return "Circle(%s, %s, %s)" % (self.pt.x, self.pt.y, self.radius)
    def __eq__(self, other):
        if not isinstance(other, Circle):
            raise ValueError("niepoprawny typ argumentu")
        return self.pt == other.pt and self.radius == other.radius
    def __ne__(self, other):
        return not self == other
    def area(self):           # pole powierzchni
        return pi*self.radius*self.radius
    def move(self, x, y):     # przesuniecie o (x, y)
        if not (isinstance(x, float) or isinstance(x, int)) and (isinstance(y, float) or isinstance(y, int)):
            raise ValueError("niepoprawny typ argumentu")
        return Circle(self.pt.x + x, self.pt.y + y, self.radius)
    def cover(self, other):   # okrąg pokrywający oba
        if not isinstance(other, Circle):
            raise ValueError("niepoprawny typ argumentu")
        R = max((self.radius+other.radius+(other.pt-self.pt).length())/2,self.radius, other.radius)
        A = R-other.radius
        B = R-self.radius
        temp = (R-self.radius)/(2*R-self.radius-other.radius)
        Y = self.pt.y + temp * (other.pt.y-self.pt.y)
        X = self.pt.x + temp * (other.pt.x-self.pt.y)
        return Circle(X, Y, R)
