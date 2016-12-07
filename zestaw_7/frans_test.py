#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from francs import Franc *

class TestFractions(unittest.TestCase):

    def test_eq_frac(self):
        self.assertTrue(Franc(1,2)==Franc(2,4))
        self.assertFalse(Franc(1,18)==Franc(2,6))
        self.assertTrue(Franc(1,2)==0.5)
        self.assertTrue(Franc(6,2)==3)
        self.assertTrue(3==Franc(6,2))
        self.assertFalse(Franc(5,2)==3)
        with self.assertRaisesRegex(ValueError, "niepoprawny typ"):
            Franc(1, 6)=="francs"   
        
    def test_neq_frac(self):
        self.assertTrue(Franc(1,2)!=Franc(1,4))
        self.assertFalse(Franc(6,18)!=Franc(2,6))
        self.assertFalse(Franc(1,2)!=0.5)
        self.assertFalse(Franc(6,2)!=3)
        self.assertTrue(Franc(5,2)!=3)
        
    def test_gt_frac(self):
        self.assertTrue(Franc(1,2)>Franc(1,4))
        self.assertFalse(Franc(6,18)>Franc(2,6))
        self.assertTrue(1>Franc(2,6))
        self.assertTrue(0.5>Franc(2,6))
        self.assertFalse(0.5>Franc(6,11))

    def test_lt_frac(self):
        self.assertFalse(Franc(1,2)<Franc(1,4))
        self.assertFalse(Franc(6,18)<Franc(2,6))
        self.assertTrue(Franc(6,18)<0.5)
        self.assertTrue(Franc(6,18)<1)
        self.assertTrue(Franc(6,18)<Franc(3,6))
        self.assertTrue(0.4<Franc(3,6))
        
    def test_le_frac(self):
        self.assertFalse(Franc(1,2)<=Franc(1,4))
        self.assertTrue(Franc(6,18)<=Franc(2,6))
        self.assertTrue(Franc(6,18)<=Franc(3,6))

    def test_ge_frac(self):
        self.assertTrue(Franc(1,2)>=Franc(1,4))
        self.assertTrue(Franc(6,18)>=Franc(2,6))
        self.assertFalse(Franc(6,18)>=Franc(3,6))
        
    def test_add_frac(self):
        self.assertEqual(Franc(1, 2)+Franc(1, 3), Franc(5, 6))
        self.assertEqual(Franc(3, 10)+Franc(1, 3), Franc(19, 30))
        self.assertEqual(Franc(3, 9)+Franc(2, 3), 1)
        self.assertEqual(0.4+Franc(1, 2), Franc(9,10))
        self.assertEqual(2+Franc(1,3), Franc(7, 3))
        with self.assertRaisesRegex(ValueError, "niepoprawny typ"):
            Franc(12, 4)+"francs"   

    def test_sub_frac(self):
        self.assertEqual(Franc(1, 2)-Franc(1, 3), Franc(1, 6))
        self.assertEqual(Franc(1,10)-0.05, Franc(1, 20))
        self.assertEqual(Franc(3,2)+1, 2.5)
        self.assertEqual(Franc(3,2)+1, Franc(5,2))
        self.assertEqual(1-Franc(3,2), Franc(-1,2))
        self.assertEqual(Franc(12, 30)-Franc(1, 3), Franc(1, 15))
        self.assertEqual(Franc(12, 30)-Franc(1, 3), Franc(1, 15))
        with self.assertRaisesRegex(ValueError, "niepoprawny typ"):
            Franc(1, 6)-"francs"   
        
    def test_mul_frac(self):
        self.assertEqual(Franc(22, 2)*Franc(1, 12), Franc(11, 12))
        self.assertEqual(Franc(12, 30)*Franc(1, 3), Franc(2, 15))
        self.assertEqual(Franc(12, 10)*2, 2.4)
        self.assertEqual(Franc(1, 10)*10, Franc(1,1))
        self.assertEqual(10*Frac(1, 6), Frac(5, 3))
        with self.assertRaisesRegex(ValueError, "niepoprawny typ"):
            Franc(1, 6)*"francs"   

    def test_div_frac(self):
        self.assertEqual(Franc(22, 2) / Franc(7, 12), Franc(132, 7))
        self.assertEqual(Franc(12, 30) / Franc(1, 3), Franc(6, 5))
        self.assertEqual(3/Franc(12, 30), Franc(30,4))
        self.assertEqual(Franc(12, 30) / 3, Franc(2, 15))
        self.assertEqual(0.5/ 3, Franc(1, 6))
        with self.assertRaisesRegex(ValueError, "niepoprawny typ"):
            Franc(1, 6)/"francs"   

    def test_frac2float(self):
        self.assertEqual(float(Franc(1,2)),0.5)
        self.assertEqual(float(Franc(3,8)),0.375)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
