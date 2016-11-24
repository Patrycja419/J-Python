#W pliku triangles.py zdefiniować klasę Triangle wraz z potrzebnymi metodami. Trójkąt jest określony przez podanie trzech wierzchołków. Napisać kod testujący moduł triangles.

from points import Point

class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1=0, y1=0, x2=0, y2=0, x3=0, y3=0):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self): pass         # "[(x1, y1), (x2, y2), (x3, y3)]"

    def __repr__(self): pass        # "Triangle(x1, y1, x2, y2, x3, y3)"

    def __eq__(self, other): pass   # obsługa tr1 == tr2

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def center(self): pass          # zwraca środek trójkąta

    def area(self): pass            # pole powierzchni

    def move(self, x, y): pass      # przesunięcie o (x, y)

