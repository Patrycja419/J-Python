# Kod testujący moduł.
#!/usr/bin/python

from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):       # "[(x1, y1), (x2, y2)]"
	self.pt1=Point(x1, y1)
	self.pt1= Point(x2, y2)
    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
	self.Rectangle=Point(x1, y1)
	self.Rectangle=Point(x2, y2)
    def __eq__(self, other):  # obsługa rect1 == rect2
	self.


    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):         # zwraca środek prostokąta
	return Point(self.x + other.x, self.y + other.y)

    def area(self): pass            # pole powierzchni

    def move(self, x, y): pass      # przesunięcie o (x, y)

