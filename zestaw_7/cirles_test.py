#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from cirles import Circle
from math import pi

class TestCircles(unittest.TestCase):
    def test_init_circles(self):
        with self.assertRaisesRegexp(ValueError, "promień ujemny"):
            Circle(1,1, -1)
        with self.assertRaisesRegexp(ValueError, "niepoprawny typ"):
            Circle(1,1, "circle")
            
    def test_eq_circles(self):
        self.assertTrue(Circle(1, 2, 5)==Circle(1, 2, 5))
        self.assertTrue(Circle(1, 2, 5)==Circle(1.0, 2.0, 5))
        self.assertTrue(Circle(11.13, 23.32, 6)==Circle(11.13, 23.32, 6))
        self.assertFalse(Circle(11.13, 23.32, 6)==Circle(11.13, 23.32, 2.1))
        self.assertFalse(Circle(11.13, 23.33, 3)==Circle(11.13, 23.32, 3))
        self.assertFalse(Circle(1, 5)==Circle(5, 1))
        self.assertTrue(Circle(1, 5)==Circle(1, 5))
        with self.assertRaisesRegexp(ValueError, "niepoprawny typ"):
            Circle(1, 5)=="circle"
        
    def test_ne_circles(self):
        self.assertFalse(Circle(1,2)!=Circle(1,2))
        self.assertFalse(Circle(1,2)!=Circle(1.0,2.0))
        self.assertFalse(Circle(11.13,23.32)!=Circle(11.13,23.32))
        self.assertTrue(Circle(11.13,23.33)!=Circle(11.13,23.32))
        self.assertTrue(Circle(1,5)!=Circle(5,1))
        with self.assertRaisesRegexp(ValueError, "niepoprawny typ"):
            Circle(1, 5)=="circle"

    def test_area_circles(self):
        self.assertEqual(Circle(1,1,1).area(), pi)
        self.assertEqual(Circle(1,1,4).area(), 16*pi)
        self.assertEqual(Circle(0.5,0.7,3.7).area(), Circle(1212,1232,3.7).area())
    
    def test_move_circles(self):
        self.assertEqual(Circle(0.5,0.7,3.7).move(1211.5,1231.3), Circle(1212,1232,3.7))
        self.assertEqual(Circle(1,1).move(0,0), Circle(1,1))
        self.assertEqual(Circle(1,1).move(1,2), Circle(2,3))
        with self.assertRaisesRegexp(ValueError, "niepoprawny typ"):
            Circle(1, 5).move("",1)
        
    def test_cover_circles(self): # funkcja znajduje najmniejszy okrąg, który pokrywa oba okręgi, więc możemy sprawdzić precyzyjne wyniki       
	self.assertEqual(Circle(1,1,1).cover(Circle(3,1,1)), Circle(2,1,2))
        self.assertEqual(Circle(1,1,1).cover(Circle(1,5,2)), Circle(1,3.5,3.5))
        self.assertEqual(Circle(1,1,1).cover(Circle(2,1,5)), Circle(2,1,5))
        self.assertEqual(Circle(4,6,10).cover(Circle(4,1,5)), Circle(4,6,10))
        self.assertEqual(Circle(0,0,10).cover(Circle(10,0,10)), Circle(5,0,15))
        with self.assertRaisesRegexp(ValueError, "niepoprawny typ"):
            Circle(0,0,10).cover("")
    
    def tearDown(self): 
	pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
