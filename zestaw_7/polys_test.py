#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from Polys import *

class TestFractions(unittest.TestCase):

    def test_eq_Poly(self):
        self.assertTrue(Poly(1,2)==Poly(2,4))
        self.assertFalse(Poly(1,18)==Poly(2,6))
        self.assertTrue(Poly(1,2)==0.5)
        self.assertTrue(Poly(6,2)==3)
        self.assertTrue(3==Poly(6,2))
        self.assertFalse(Poly(5,2)==3)
        with self.assertRaisesRegex(ValueError, "niepoprawny typ"):
            Poly(1, 6)=="polys"   

    def test_neq_Poly(self):
        self.assertTrue(Poly(1,2)!=Poly(1,4))
        self.assertFalse(Poly(6,18)!=Poly(2,6))
        self.assertFalse(Poly(1,2)!=0.5)
        self.assertFalse(Poly(6,2)!=3)
        self.assertTrue(Poly(5,2)!=3)        

    def test_pow_Poly(self):
        self.assert(Poly(1,2)**Poly(1,4))
        self.assert(Poly(6,18)**Poly(2,6))
        self.assert(Poly(6,18)**0.5)
        self.assertTrue(Poly(6,18)**1)
            
    def test_ge_Poly(self):
        self.assertTrue(Poly(1,2)>=Poly(1,4))
        self.assertTrue(Poly(6,18)>=Poly(2,6))
        self.assertFalse(Poly(6,18)>=Poly(3,6))
        
    def test_add_Poly(self):
        self.assertEqual(Poly(1, 2)+Poly(1, 3), Poly(5, 6))
        self.assertEqual(0.4+Poly(1, 2), Poly(9,10))
        self.assertEqual(2+Poly(1,3), Poly(7, 3))
        with self.assertRaisesRegex(ValueError, "niepoprawny typ"):
            Poly(12, 4)+"polys"   

    def test_sub_Poly(self):
        self.assertEqual(Poly(1, 2)-Poly(1, 3), Poly(1, 6))
        self.assertEqual(Poly(1,10)-0.05, Poly(1, 20))
        self.assertEqual(Poly(3,2)+1, 2.5)
        self.assertEqual(Poly(3,2)+1, Poly(5,2))
        self.assertEqual(1-Poly(3,2), (-1,2))
        self.assertEqual(Poly(12, 30)-Poly(1, 3), Poly(1, 15))
        self.assertEqual(Poly(12, 30)-Poly(1, 3), Poly(1, 15))
        with self.assertRaisesRegex(ValueError, "niepoprawny typ"):
            Frac(1, 6)-"polys"   
        
    def test_mul_Poly(self):
        self.assertEqual(Poly(22, 2)*Poly(1, 12), Poly(11, 12))
        self.assertEqual(Poly(12, 30)*Poly(1, 3), Poly(2, 15))
        self.assertEqual(Poly(12, 10)*2, 2.4)
        self.assertEqual(Poly(1, 10)*10, Poly(1,1))
        self.assertEqual(10*Poly(1, 6), Poly(5, 3))
        with self.assertRaisesRegex(ValueError, "niepoprawny typ"):
            Poly(1, 6)*"polys"  

    def test_div_Poly(self):
        self.assertEqual(Poly(22, 2) / Poly(7, 12), Poly(132, 7))
        self.assertEqual(Poly(12, 30) / Poly(1, 3), Poly(6, 5))
        self.assertEqual(3/Poly(12, 30), Poly(30,4))
        self.assertEqual(Poly(12, 30) / 3, Poly(2, 15))
        self.assertEqual(0.5/ 3, Poly(1, 6))
        with self.assertRaisesRegex(ValueError, "niepoprawny typ"):
            Poly(1, 6)"polys"   

    def test_Poly2float(self):
        self.assertEqual(float(Poly(1,2)),0.5)
        self.assertEqual(float(Poly(3,8)),0.375)


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
