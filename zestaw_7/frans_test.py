#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from fracs import *

class TestFractions(unittest.TestCase):

    def test_eq_frac(self):
        self.assertTrue(Frac(1,2)==Frac(2,4))
        self.assertFalse(Frac(1,18)==Frac(2,6))
        self.assertTrue(Frac(1,2)==0.5)
        self.assertTrue(Frac(6,2)==3)
        self.assertTrue(3==Frac(6,2))
        self.assertFalse(Frac(5,2)==3)
        with self.assertRaisesRegex(ValueError, "niepoprawny typ"):
            Frac(1, 6)=="lubię placki"   
        
    def test_neq_frac(self):
        self.assertTrue(Frac(1,2)!=Frac(1,4))
        self.assertFalse(Frac(6,18)!=Frac(2,6))
        self.assertFalse(Frac(1,2)!=0.5)
        self.assertFalse(Frac(6,2)!=3)
        self.assertTrue(Frac(5,2)!=3)
        
    def test_gt_frac(self):
        self.assertTrue(Frac(1,2)>Frac(1,4))
        self.assertFalse(Frac(6,18)>Frac(2,6))
        self.assertTrue(1>Frac(2,6))
        self.assertTrue(0.5>Frac(2,6))
        self.assertFalse(0.5>Frac(6,11))

    def test_lt_frac(self):
        self.assertFalse(Frac(1,2)<Frac(1,4))
        self.assertFalse(Frac(6,18)<Frac(2,6))
        self.assertTrue(Frac(6,18)<0.5)
        self.assertTrue(Frac(6,18)<1)
        self.assertTrue(Frac(6,18)<Frac(3,6))
        self.assertTrue(0.4<Frac(3,6))
        
    def test_le_frac(self):
        self.assertFalse(Frac(1,2)<=Frac(1,4))
        self.assertTrue(Frac(6,18)<=Frac(2,6))
        self.assertTrue(Frac(6,18)<=Frac(3,6))

    def test_ge_frac(self):
        self.assertTrue(Frac(1,2)>=Frac(1,4))
        self.assertTrue(Frac(6,18)>=Frac(2,6))
        self.assertFalse(Frac(6,18)>=Frac(3,6))
        
    def test_add_frac(self):
        self.assertEqual(Frac(1, 2)+Frac(1, 3), Frac(5, 6))
        self.assertEqual(Frac(3, 10)+Frac(1, 3), Frac(19, 30))
        self.assertEqual(Frac(3, 9)+Frac(2, 3), 1)
        self.assertEqual(0.4+Frac(1, 2), Frac(9,10))
        self.assertEqual(2+Frac(1,3), Frac(7, 3))
        with self.assertRaisesRegex(ValueError, "niepoprawny typ"):
            Frac(12, 4)+"lubię placki"   

    def test_sub_frac(self):
        self.assertEqual(Frac(1, 2)-Frac(1, 3), Frac(1, 6))
        self.assertEqual(Frac(1,10)-0.05, Frac(1, 20))
        self.assertEqual(Frac(3,2)+1, 2.5)
        self.assertEqual(Frac(3,2)+1, Frac(5,2))
        self.assertEqual(1-Frac(3,2), Frac(-1,2))
        self.assertEqual(Frac(12, 30)-Frac(1, 3), Frac(1, 15))
        self.assertEqual(Frac(12, 30)-Frac(1, 3), Frac(1, 15))
        with self.assertRaisesRegex(ValueError, "niepoprawny typ"):
            Frac(1, 6)-"lubię placki"   
        
    def test_mul_frac(self):
        self.assertEqual(Frac(22, 2)*Frac(1, 12), Frac(11, 12))
        self.assertEqual(Frac(12, 30)*Frac(1, 3), Frac(2, 15))
        self.assertEqual(Frac(12, 10)*2, 2.4)
        self.assertEqual(Frac(1, 10)*10, Frac(1,1))
        self.assertEqual(10*Frac(1, 6), Frac(5, 3))
        with self.assertRaisesRegex(ValueError, "niepoprawny typ"):
            Frac(1, 6)*"lubię placki"   

    def test_div_frac(self):
        self.assertEqual(Frac(22, 2) / Frac(7, 12), Frac(132, 7))
        self.assertEqual(Frac(12, 30) / Frac(1, 3), Frac(6, 5))
        self.assertEqual(3/Frac(12, 30), Frac(30,4))
        self.assertEqual(Frac(12, 30) / 3, Frac(2, 15))
        self.assertEqual(0.5/ 3, Frac(1, 6))
        with self.assertRaisesRegex(ValueError, "niepoprawny typ"):
            Frac(1, 6)/"lubię placki"   

    def test_frac2float(self):
        self.assertEqual(float(Frac(1,2)),0.5)
        self.assertEqual(float(Frac(3,8)),0.375)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
