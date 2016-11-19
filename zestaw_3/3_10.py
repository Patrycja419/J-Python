#!/usr/bin/python
# -*- coding: utf-8 -*-

#-----------------------------------------#
# równoważne metody tworzenia słownika
#-----------------------------------------#
# metoda 1
slownik = {};
slownik.update({'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000});
# metoda 2
slownik = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000};
# metoda 3
slownik = {};
slownik['I'] = 1;
slownik['V'] = 5;
slownik['X'] = 10;
slownik['L'] = 50;
slownik['C'] = 100;
slownik['D'] = 500;
slownik['M'] = 1000;
#metoda 4
slownik = dict(zip(['I', 'V', 'X', 'L', 'C', 'D', 'M'], [1, 5, 10, 50, 100, 500, 1000]));
#-----------------------------------------#

def roman2int( r ):
 ret = 0;
 temp = 0;
 poprzedniZnak = r[0];
 for aktualnyZnak in r[1:]:
  if(slownik[poprzedniZnak] > slownik[aktualnyZnak]):
   ret += slownik[poprzedniZnak] + temp;
   temp = 0;
  elif(poprzedniZnak == aktualnyZnak):
   temp += slownik[poprzedniZnak];
  else:
   temp = poprzedniZnak - temp;
  poprzedniZnak = aktualnyZnak;
 ret += temp + slownik[r[len(r)-1]];
 return ret;
 
get = raw_input();
print roman2int( get );
