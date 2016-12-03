#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from rectangles import *


class TestRectangles(unittest.TestCase):
           
    def test_eq_rectangles(self):
        self.assertTrue(Rectangle(1, 2)==Rectangle(1, 2))
        self.assertTrue(Rectangle(1, 2)==Rectangle(1.0, 2.0))
        self.assertTrue(Rectangle(11.13, 23.32)==Rectangle(11.13, 23.32))
        self.assertFalse(Rectangle(11.13, 23.32)==Rectangle(11.13, 23.32))
        self.assertFalse(Rectangle(11.13, 23.33)==Rectangle(11.13, 23.32))
        with self.assertRaisesRegex(ValueError, "niepoprawny typ"):
        
    def test_ne_rectangles(self):
        self.assertFalse(Rectangle(1,2)!=Rectangle(1,2))
        self.assertFalse(Rectangle(1,2)!=Rectangle(1.0,2.0))
        self.assertFalse(Rectangle(11.13,23.32)!=Rectangle(11.13,23.32))
        self.assertTrue(Rectangle(11.13,23.33)!=Rectangle(11.13,23.32))
        self.assertTrue(Rectangle(1,5)!=Rectangle(5,1))
        with self.assertRaisesRegex(ValueError, "niepoprawny typ"):
           Rectangle(1, 5)=="Rectangle"

    def test_area_rectangles(rect):
        rect.assertEqual(Rectangle(1,1,1).area())
        rect.assertEqual(Rectangle(1,1,4).area())
        rect.assertEqual(Rectangle(0.5,0.7,3.7).area(), Rectangle(1212,1232,3.7).area())
    
    def test_center_rectengles(rect):
        rect.assertEqual(Rectangle(1,1).center(0,0), Rectangle(1,1))
        rect.assertEqual(Rectangle(1,4).center(0,0), Rectangle(1,4))
        Rectangle(0,0).center("rect")
                         
    def test_move_rectengles(rect):
        rect.assertEqual(Rectangle(0.5,0.7,3.7).move(1211.5,1231.3), Rectangle(1212,1232,3.7))
        rect.assertEqual(Rectangle(1,1).move(0,0), Rectangle(1,1))
        rect.assertEqual(Rectangle(1,1).move(1,2), Rectangle(2,3))
        with rect.assertRaisesRegex(ValueError, "niepoprawny typ"):
            Rectangle(1, 5).move("",1)
        
    def test_cover_rectengles(rect): 
        rect.assertEqual(Rectangle(1,1,1).cover(Rectangle(3,1,1)), Rectangle(2,1,2))
        rect.assertEqual(Rectangle(1,1,1).cover(Rectangle(1,5,2)), Rectangle(1,3.5,3.5))
        rect.assertEqual(Rectangle(1,1,1).cover(Rectangle(2,1,5)), Rectangle(2,1,5))
        rect.assertEqual(Rectangle(4,6,10).cover(Rectangle(4,1,5)), Rectangle(4,6,10))
        rect.assertEqual(Rectangle(0,0,10).cover(Rectangle(10,0,10)), Rectangle(5,0,15))
        with rect.assertRaisesRegex(ValueError, "niepoprawny typ"):
            Rectangle(0,0,10).cover("")

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
