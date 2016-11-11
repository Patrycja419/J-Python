#!/usr/bin/python
# -*- coding: utf-8 -*-
import math;

def miarka ( dl ):
    if(dl >= 10000):
        return ""
    wy = "|"
    for i in range(1,dl+1):
        wy += "....|"
    wy += "\n0"
    for i in range(1,dl+1):
        for j in range(4-int(math.floor(math.log(i,10)))):
            wy += ' '
        wy += str(i);
    return wy

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
 
def prostokat ( x, y ):
    wy = liniaPozioma1(x)+"\n";
    for i in range(y):
        wy += liniaPozioma2(x)+"\n"+liniaPozioma1(x)+"\n";
    return wy
        
		
print (miarka(4)+"\n")
print (prostokat(4,4))
