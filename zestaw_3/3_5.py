#!/usr/bin/python

import math;
print "Podaj dlugosc miarki:";
try:
 dl = int(raw_input());
except (NameError, SyntaxError, ValueError) as e:
 print 'Niepoprawna wartosc!!';
 exit();

if(dl >= 10000):
 print 'Podana wartosc jest zbyt duza!!';
 exit();
 
wy = "|"
for i in range(1,dl+1):
 wy += "....|"
wy += "\n0"
for i in range(1,dl+1):
 for j in range(4-int(math.floor(math.log(i,10)))):
  wy += ' '
 wy += str(i);
 
 
print wy;
