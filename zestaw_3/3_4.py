#!/usr/bin/python

n = raw_input();
while(n != "stop"):
 try:
  p = pow(float(n),3);
  print n, p;
 except ValueError:
  print 'blad: nie jest to liczba';
 n = raw_input();
