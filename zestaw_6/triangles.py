#!/usr/bin/python
# -*- coding: utf-8 -*-

from points import Point

class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1=0, y1=0, x2=0, y2=0, x3=0, y3=0):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self): pass         # "[(x1, y1), (x2, y2), (x3, y3)]"
        return "(%s, %s)" % (self.x1, self.y1)
        return "(%s, %s)" % (self.x2, self.y2)
        return "(%s, %s)" % (self.x3, self.y3)

    def __repr__(self):       # "Triangle(x1, y1, x2, y2, x3, y3)"
    return "Triangle(%s, %s)" % (self.x1, self.y1)
    return "Triangle(%s, %s)" % (self.x2, self.y2)
    return "Triangle(%s, %s)" % (self.x3, self.y3)

    def __eq__(self, other):  # obsługa tr1 == tr2  
    if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def center(self): # zwraca środek trójkąta
	x = self.corner.x + self.width/2.0
	y = self.corner.y + self.height/2.0
	center = Point()
	set_point(center, x, y)
	return center

    def area(self):             # pole powierzchni
	return self.width * self.height/2.0

    def move(self, x, y):      # przesunięcie o (x, y)
    return self.width+x
	return self.height+y
