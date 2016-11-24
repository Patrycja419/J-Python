#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from fracs import *

class TestFractions(unittest.TestCase):

    def setUp(self):

    def test_eq_frac(self):
        self.assertTrue(Frac(1,2)==Frac(2,4))
        self.assertFalse(Frac(1,18)==Frac(2,6))
        
    def test_neq_frac(self):
        self.assertTrue(Frac(1,2)!=Frac(1,4))
        self.assertFalse(Frac(6,18)!=Frac(2,6))
        
    def test_gt_frac(self):
        self.assertTrue(Frac(1,2)>Frac(1,4))
        self.assertFalse(Frac(6,18)>Frac(2,6))

    def test_lt_frac(self):
        self.assertFalse(Frac(1,2)<Frac(1,4))
        self.assertFalse(Frac(6,18)<Frac(2,6))
        self.assertTrue(Frac(6,18)<Frac(3,6))
        
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

    def test_sub_frac(self):
        self.assertEqual(Frac(1, 2)-Frac(1, 3), Frac(1, 6))
        self.assertEqual(Frac(12, 30)-Frac(1, 3), Frac(1, 15))

    def test_mul_frac(self):
        self.assertEqual(Frac(22, 2)*Frac(1, 12), Frac(11, 12))
        self.assertEqual(Frac(12, 30)*Frac(1, 3), Frac(2, 15))

    def test_div_frac(self):
        self.assertEqual(Frac(22, 2) / Frac(7, 12), Frac(132, 7))
        self.assertEqual(Frac(12, 30) / Frac(1, 3), Frac(6, 5))

    def test_is_positive(self): pass

    def test_frac2float(self):
        self.assertEqual(float(Frac(1,2)),0.5)
        self.assertEqual(float(Frac(3,8)),0.375)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy

