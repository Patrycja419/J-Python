# Kod testujący moduł.
#!/usr/bin/python

from points import Point

class Point:
    "
    pass

class Rectangle:

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()          # obiekt Point jest zagnieżdżony w obiekcie Rectangle
box.corner.x = 0.0            # określamy atrybuty punktu
box.corner.y = 0.0

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):       # "[(x1, y1), (x2, y2)]"
	self.pt1=Point(x1, y1)
	self.pt1= Point(x2, y2)
    def __repr__(rect):        # "Rectangle(x1, y1, x2, y2)"
	self.Rectangle=rect(x1, y1)
	self.Rectangle=rect(x2, y2)
    def __eq__(rect, other):  # obsługa rect1 == rect2
	return (rect1.x1== rect2.x2) and (rect1.y1== rect2.y2)


    def __ne__(rect, other):        # obsługa rect1 != rect2
        return not self == other

    def set_rect(rect, x, y, w, h):
	rect.width = w
	rect.height = h
	rect.corner = Point()
    set_point(rect.corner, x, y)

    def center(rect):         # zwraca środek prostokąta
	x = rect.corner.x + rect.width/2.0
	y = rect.corner.y + rect.height/2.0
	center = Point()
	set_point(center, x, y)
	return center

    def area(rect):            # pole powierzchni
	return rect.width * rect.height
    def move(self, x, y): pass      # przesunięcie o (x, y)

