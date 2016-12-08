#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from Triangles import Triangle

class TestTirgles(unittest.TestCase):
	def test_eq_Triangles(self):pass
		self.assertTrue(Triangle(1, 2, 5)==(1, 2, 5)
		self.assertFalse(Triangle(11.13, 23.32, 6)==Triangle(11.13, 23.32, 2.1))
 		self.assertFalse(Triangle(11.13, 23.33, 3)==Triangle(11.13, 23.32, 3))
 		self.assertFalse(Triangle(1, 5)==Triangle(5, 1))
 		self.assertTrue(Triangle(1, 5)==Triangle(1, 5))
		with self.assertRaisesRegexp(ValueError, "niepoprawny typ"):
		Triangle(1, 5)=="Triangle"
        
	def test_ne_Triangles(self):
		self.assertFalse(Triangle(1,2)!=Triangle(1,2))
		self.assertFalse(Triangle(1,2)!=Triangle(1.0,2.0))
		self.assertFalse(Triangle(11.13,23.32)!=Triangle(11.13,23.32))
		self.assertTrue(Triangle(11.13,23.33)!=Triangle(11.13,23.32))
		self.assertTrue(Triangle(1,5)!=Triangle(5,1))
		with self.assertRaisesRegexp(ValueError, "niepoprawny typ"):
		Triangle(1, 5)=="Triangle"
            
	def test_area_Triangles(self):
		self.assertEqual(Triangle(1,1,1).area())
		self.assertEqual(Triangle(1,1,4).area())
		self.assertEqual(Triangle(0.5,0.7,3.7).area(), Triangle(1212,1232,3.7).area())
    
	def test_move_Triangles(self):
		self.assertEqual(Triangle(0.5,0.7,3.7).move(1211.5,1231.3), Triangle(1212,1232,3.7))
		self.assertEqual(Triangle(1,1).move(0,0), Triangle(1,1))
		self.assertEqual(Triangle(1,1).move(1,2), Triangle(2,3))
		with self.assertRaisesRegexp(ValueError, "niepoprawny typ"):
		Triangle(1, 5).move("",1)
        
	def test_center_Triangles(self):        
		self.assertEqual(Triangle(1,1,3).center(0,0,0), Triangle(1,1,3))
		self.assertEqual(Triangle(1,4,3).center(0,0,0), Triangle(1,4,3))
		Triangle(0,0,0).center("tirangle")    
	def make4(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
