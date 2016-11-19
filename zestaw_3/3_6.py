#!/usr/bin/python
# -*- coding: utf-8 -*-

def liniaPozioma1( liczbaKratek ):
 ret = "+";
 for i in range(liczbaKratek):
  ret += "---+";
 return ret;

def liniaPozioma2( liczbaKratek ):
 ret = "|";
 for i in range(liczbaKratek):
  ret += "   |";
 return ret;
 
print "Podaj liczbe kratek w poziomie:";
try:
 x = int(raw_input());
except (NameError, SyntaxError, ValueError) as e:
 print 'Niepoprawna wartosc!!';
 exit();

print "Podaj liczbe kratek w pionie:";
try:
 y = int(raw_input());
except (NameError, SyntaxError, ValueError) as e:
 print 'Niepoprawna wartosc!!';
 exit();

 
wy = liniaPozioma1(x)+"\n";
for i in range(y):
 wy += liniaPozioma2(x)+"\n"+liniaPozioma1(x)+"\n";
 
 
print wy;
