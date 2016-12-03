#!/usr/bin/python
# -*- coding: utf-8 -*-

from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
    # Chcemy, aby x1 <= x2, y1 <= y2.
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):         # "[(x1, y1), (x2, y2)]"
        return "(%s, %s)" % (self.x1, self.y1)
        return "(%s, %s)" % (self.x2, self.y2)
    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        self.Rectangle=rect(x1, y1)
        self.Rectangle=rect(x2, y2)
    def __eq__(self, other):   # obsługa rect1 == rect2
        return (rect1.x1== rect2.x2) and (rect1.y1== rect2.y2)
    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(rect):           # zwraca środek prostokąta
        x = rect.corner.x + rect.width/2.0
        y = rect.corner.y + rect.height/2.0
        center = Point()
        set_point(center, x, y)
        return center
    def area(srect):            # pole powierzchni
        return rect.width * rect.height
        def move(rect, x, y): 
    
    def move(rect, x, y):       # przesunięcie o (x, y)
        return rect.width+x
        return rect.height+y

    def intersection(self, other): pass # część wspólna prostokątów
        return (self.x1)*(self.x2)=(other.y2)*(other.y2)
    def cover(self, other): pass    # prostąkąt nakrywający oba
        
    def make4(self): pass           # zwraca listę czterech mniejszych
