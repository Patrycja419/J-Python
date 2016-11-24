# Kod testujący moduł.
#!/usr/bin/python
# -*- coding: utf-8 -*- 

import unittest

class TestTime(unittest.TestCase):

    def setUp(self): pass

    def test_print(self): pass      # test str() i repr()

    def test_add(self):
        self.assertEqual(Time(1) + Time(2), Time(3))

    def test_cmp(self):
        # Można sprawdzać ==, !=, >, >=, <, <=.
        self.assertTrue(Time(1) == Time(1))
        self.assertTrue(Time(1) != Time(2))
        self.assertTrue(Time(3) > Time(2))

    def test_int(self): pass

    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()     # wszystkie testy

