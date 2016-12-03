#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from tiragles import *

class TestCircles(unittest.TestCase):
            
    def test_eq_tiragles(self):
        self.assertTrue(Tiragle(1, 2, 5)==Tiragle(1, 2, 5))
        self.assertTrue(Tiragle(1, 2, 5)==Tiragle(1.0, 2.0, 5))
        self.assertTrue(Tiragle(11.13, 23.32, 6)==Tiragle(11.13, 23.32, 6))
        self.assertFalse(Tiragle(11.13, 23.32, 6)==Tiragle(11.13, 23.32, 2.1))
        self.assertFalse(Tiragle(11.13, 23.33, 3)==Tiragle(11.13, 23.32, 3))
        self.assertFalse(Tiragle(1, 5)==Tiragle(5, 1))
        self.assertTrue(Tiragle(1, 5)==Tiragle(1, 5))
        with self.assertRaisesRegex(ValueError, "niepoprawny typ"):
            Tiraglee(1, 5)=="Tiragle"
        
    def test_ne_tiragles(self):
        self.assertFalse(Tiragle(1,2)!=Tiragle(1,2))
        self.assertFalse(Tiragle(1,2)!=Tiragle(1.0,2.0))
        self.assertFalse(Tiragle(11.13,23.32)!=Tiragle(11.13,23.32))
        self.assertTrue(Tiragle(11.13,23.33)!=Tiragle(11.13,23.32))
        self.assertTrue(Tiragle(1,5)!=Tiragle(5,1))
        with self.assertRaisesRegex(ValueError, "niepoprawny typ"):
            Tiragle(1, 5)=="Tiragle"

    def test_area_circles(self):
        self.assertEqual(Tiragle(1,1,1).area())
        self.assertEqual(Tiragle(1,1,4).area())
        self.assertEqual(Tiragle(0.5,0.7,3.7).area(), Tiragle(1212,1232,3.7).area())
    
    def test_move_tiragles(self):
        self.assertEqual(Tiragle(0.5,0.7,3.7).move(1211.5,1231.3), Tiragle(1212,1232,3.7))
        self.assertEqual(Tiragle(1,1).move(0,0), Tiragle(1,1))
        self.assertEqual(Tiragle(1,1).move(1,2), Tiragle(2,3))
        with self.assertRaisesRegex(ValueError, "niepoprawny typ"):
            Tiragle(1, 5).move("",1)
    def test_center_tiragles(self):        
        self.assertEqual(Tiragle(1,1,3).center(0,0,0), Tiragle(1,1,3))
        self.assertEqual(Tiragle(1,4,3).center(0,0,0), Tiragle(1,4,3))
        Tiragle(0,0,0).center("tirangle")    
    def make4(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
