#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from rectangles import Rectangle


class TestRectangles(unittest.TestCase):
           
    def test_eq_Rectangles(self):
        self.assertTrue(Rectangle(1, 2)==Rectangle(1, 2))
        self.assertTrue(Rectangle(1, 2)==Rectangle(1.0, 2.0))
        self.assertTrue(Rectangle(11.13, 23.32)==Rectangle(11.13, 23.32))
        self.assertFalse(Rectangle(11.13, 23.32)==Rectangle(11.13, 23.32))
        self.assertFalse(Rectangle(11.13, 23.33)==Rectangle(11.13, 23.32))
        with self.assertRaisesRegexp(ValueError, "niepoprawny typ"):
        
    def test_ne_Rectangles(self):
        self.assertFalse(Rectangle(1,2)!=Rectangle(1,2))
        self.assertFalse(Rectangle(1,2)!=Rectangle(1.0,2.0))
        self.assertTrue(Rectangle(11.13,23.33)!=Rectangle(11.13,23.32))
        self.assertTrue(Rectangle(1,5)!=Rectangle(5,1))
        with self.assertRaisesRegexp(ValueError, "niepoprawny typ"):
           Rectangle(1, 5)=="Rectangle"

    def test_area_Rectangles(rect):
        rect.assertEqual(Rectangle(1,1,1).area())
        rect.assertEqual(Rectangle(1,1,4).area())
        rect.assertEqual(Rectangle(0.5,0.7,3.7).area(), Rectangle(1212,1232,3.7).area())
    
    def test_center_Rectangles(rect):
        rect.assertEqual(Rectangle(1,1).center(0,0), Rectangle(1,1))
        rect.assertEqual(Rectangle(1,4).center(0,0), Rectangle(1,4))
        Rectangle(0,0).center("rect")
                         
    def test_move_Rectangles(rect):pass
        rect.assertEqual(Rectangle(0.5,0.7,3.7).move(1211.5,1231.3), Rectangle(1212,1232,3.7))
        rect.assertEqual(Rectangle(1,1).move(0,0), Rectangle(1,1))
        rect.assertEqual(Rectangle(1,1).move(1,2), Rectangle(2,3))
        with rect.assertRaisesRegexp(ValueError, "niepoprawny typ"):
            Rectangle(1, 5).move("",1)
        
   
if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy

