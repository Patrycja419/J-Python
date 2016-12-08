#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from francs import Fraction
from fractions import Fraction
from math import pi
class TestFraction(unittest.TestCase):

    def test_eq_Fraction(self):
        self.assertTrue(Fraction(1,2)==Fraction(2,4))
        self.assertFalse(Fraction(1,18)==Fraction(2,6))
        self.assertTrue(Fraction(1,2)==0.5)
        self.assertTrue(Fraction(6,2)==3)
        self.assertTrue(3==Fraction(6,2))
        self.assertFalse(Fraction(5,2)==3)
        with self.assertRaisesRegexp(ValueError, "niepoprawny typ"):
            Fraction(1, 6)=="Fractions"   
        
    def test_neq_Fraction(self):
        self.assertTrue(Fraction(1,2)!=Fraction(1,4))
        self.assertFalse(Fraction(6,18)!=Fraction(2,6))
        self.assertFalse(Fraction(1,2)!=0.5)
        self.assertFalse(Fraction(6,2)!=3)
        self.assertTrue(Fraction(5,2)!=3)
        
    def test_gt_Fraction(self):
        self.assertTrue(Fraction(1,2)>Fraction(1,4))
        self.assertFalse(Fraction(6,18)>Fraction(2,6))
        self.assertTrue(1>Fraction(2,6))
        self.assertTrue(0.5>Fraction(2,6))
        self.assertFalse(0.5>Fraction(6,11))

    def test_lt_Fraction(self):
        self.assertFalse(Fraction(1,2)<Fraction(1,4))
        self.assertFalse(Fraction(6,18)<Fraction(2,6))
        self.assertTrue(Fraction(6,18)<0.5)
        self.assertTrue(Fraction(6,18)<1)
        self.assertTrue(Fraction(6,18)<Fraction(3,6))
        self.assertTrue(0.4<Fraction(3,6))
        
    def test_le_Fraction(self):
        self.assertFalse(Fraction(1,2)<=Fraction(1,4))
        self.assertTrue(Fraction(6,18)<=Fraction(2,6))
        self.assertTrue(Fraction(6,18)<=Fraction(3,6))

    def test_ge_Fraction(self):
        self.assertTrue(Fraction(1,2)>=Fraction(1,4))
        self.assertTrue(Fraction(6,18)>=Fraction(2,6))
        self.assertFalse(Fraction(6,18)>=Fraction(3,6))
        
    def test_add_Fraction(self):
        self.assertEqual(Fraction(1, 2)+Fraction(1, 3), Fraction(5, 6))
        self.assertEqual(Fraction(3, 10)+Fraction(1, 3), Fraction(19, 30))
        self.assertEqual(Fraction(3, 9)+Fraction(2, 3), 1)
        self.assertEqual(0.4+Fraction(1, 2), Fraction(9,10))
        self.assertEqual(2+Fraction(1,3), Fraction(7, 3))
        with self.assertRaisesRegexp(ValueError, "niepoprawny typ"):
            Fraction(12, 4)+"Fractions"   

    def test_sub_Fraction(self):
        self.assertEqual(Fraction(1, 2)-Fraction(1, 3), Fraction(1, 6))
        self.assertEqual(Fraction(1,10)-0.05, Fraction(1, 20))
        self.assertEqual(Fraction(3,2)+1, 2.5)
        self.assertEqual(Fraction(3,2)+1, Fraction(5,2))
        self.assertEqual(1-Fraction(3,2), Fraction(-1,2))
        self.assertEqual(Fraction(12, 30)-Fraction(1, 3), Fraction(1, 15))
        self.assertEqual(Fraction(12, 30)-Fraction(1, 3), Fraction(1, 15))
        with self.assertRaisesRegexp(ValueError, "niepoprawny typ"):
            Fraction(1, 6)-"Fractions"   
        
    def test_mul_Fraction(self):
        self.assertEqual(Fraction(22, 2)*Fraction(1, 12), Fraction(11, 12))
        self.assertEqual(Fraction(12, 30)*Fraction(1, 3), Fraction(2, 15))
        self.assertEqual(Fraction(12, 10)*2, 2.4)
        self.assertEqual(Fraction(1, 10)*10, Fraction(1,1))
        self.assertEqual(10*Fraction(1, 6), Fraction(5, 3))
        with self.assertRaisesRegexp(ValueError, "niepoprawny typ"):
            Fraction(1, 6)*"Fractions"   

    def test_div_Fraction(self):
        self.assertEqual(Fraction(22, 2) / Fraction(7, 12), Fraction(132, 7))
        self.assertEqual(Fraction(12, 30) / Fraction(1, 3), Fraction(6, 5))
        self.assertEqual(3/Fraction(12, 30), Fraction(30,4))
        self.assertEqual(Fraction(12, 30) / 3, Fraction(2, 15))
        self.assertEqual(0.5/ 3, Fraction(1, 6))
        with self.assertRaisesRegexp(ValueError, "niepoprawny typ"):
            Fraction(1, 6)/"Fractions"   

    def test_Fraction2float(self):
        self.assertEqual(float(Fraction(1,2)),0.5)
        self.assertEqual(float(Fraction(3,8)),0.375)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
