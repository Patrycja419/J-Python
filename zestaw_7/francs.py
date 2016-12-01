#!/usr/bin/python
# -*- coding: utf-8 -*-


class Frac:
    def __init__(self, x=0, y=1):
        if x%1 == 0 and y%1 == 0:
            if y == 0:
                raise ValueError("zerowy mianownik")
            self.x = int(x)
            self.y = int(y)
        elif isinstance(x, float):
            args = x.as_integer_ratio()
            self.x = int(args[0])
            self.y = int(args[1])
        elif isinstance(x, int):
            args = x.as_integer_ratio()
            self.x = x
            self.y = 1
        else:
            raise ValueError("niepoprawny typ argumentów")
        
    def __str__(self):
        if self.y==1:
            return str(self.x)
        else:
            return str(self.x)+'/'+str(self.y)
        
    def __repr__(self):
        return "Frac(%s, %s)" % (self.x, self.y)
    
    def __add__(self, other):               # frac1+frac2, frac+int
        other = self.otherToFrac(other)
        lcm = int(self.y*other.y/gcd(self.y, other.y))
        ret = [int(self.x*lcm/self.y+other.x*lcm/other.y), lcm]
        divider = gcd(ret[0], ret[1])
        return  Frac(ret[0]/divider, ret[1]/divider)
        
    __radd__ = __add__                      # int+frac
    
    def __sub__(self, other):               # frac1-frac2, frac-int
        other = self.otherToFrac(other)
        return self+(-other)
        
    def __rsub__(self, other):              # int-frac
        other = self.otherToFrac(other)
        return other-self
        
    def __mul__(self, other):               # frac1 * frac2
        other = self.otherToFrac(other)
        ret = [self.x*other.x, self.y*other.y]
        divider = gcd(ret[0], ret[1])
        return Frac(ret[0]/divider, ret[1]/divider)
        
    __rmul__ = __mul__                      # int*frac
        
    #ta metoda zastąpiła __div__
    def __truediv__(self, other):           # frac1 / frac2
        other = self.otherToFrac(other)
        return self*~other
        
    def __rtruediv__(self, other):          # int/frac
        other = self.otherToFrac(other)
        return other/self
        
    def __pos__(self):  # +frac
        return self
        
    def __neg__(self):  # -frac
        return Frac(-self.x, self.y)
        
    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)
        
    # metoda nie obsługiwana przez Pythona 3
    def __cmp__(self, other):             # -1 | 0 | +1
        other = self.otherToFrac(other)
        sub = self-other
        if sub.x == 0: # self = sother
            return 0
        elif sub.x*sub.y > 0: # self > other
            return 1
        else: # self < other
            return -1   
            
    def __eq__(self,other):
        other = self.otherToFrac(other)
        sub = self-other
        if sub.x == 0: # self = other
            return True
        else:
            return False
    
    def __neq__(self,other):
        other = self.otherToFrac(other)
        if self == other:
            return False
        else:
            return True
            
    def __lt__(self,other):
        other = self.otherToFrac(other)
        sub = self-other
        if sub.x*sub.y >= 0: # self >= other
            return False
        else:
            return True # self < other
    
    def __gt__(self,other):
        other = self.otherToFrac(other)
        sub = self-other
        if sub.x*sub.y > 0: # self > other
            return True
        else:
            return False
            
    def __le__(self,other):
        other = self.otherToFrac(other)
        sub = self-other
        if sub.x*sub.y > 0: # self > other
            return False
        else:
            return True # self <= other
    
    def __ge__(self,other):
        other = self.otherToFrac(other)
        sub = self-other
        if sub.x*sub.y >= 0: # self >= other
            return True
        else:
            return False
  
    def __float__(self):                   # konwersja do float
        return float(self.x)/float(self.y)
        
    def otherToFrac(self,x):
        if isinstance(x, Frac):
            return x
        elif isinstance(x, float) or isinstance(x, int):
            return Frac(x)
        else:
            raise ValueError("niepoprawny typ argumentów")

