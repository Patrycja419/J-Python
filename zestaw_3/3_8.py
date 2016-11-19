#!/usr/bin/python
# -*- coding: utf-8 -*-
import math;

# tuple
t1 = (1,2,3,4);
t2 = (3,4,5,6);

t3 = t1+t2;
wspolne = set();
powt = set();

for a in t3:
 if a not in wspolne:
  wspolne.add(a);
 else:
  powt.add(a);

print 'Sekwencja nr 1:';
print t1;
print 'Sekwencja nr 2:';
print t2;
print 'Wszystkie elementy:';
print list(wspolne);
print 'Powtarzajace sie:';
print list(powt);
