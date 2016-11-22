#!/usr/bin/python
# -*- coding: utf-8 -*-
import rekurencja # importuje pakiet ze ścieżką rekurencja.
print (rekurencja.factorial(6))
print (rekurencja.fibonacci(5))

import rekurencja as rek # importuje pakiet ze ścieżką rek. zamiast rekurencja.
print (rek.factorial(6))
print (rek.fibonacci(5))

from rekurencja import * #importuje wszystkie funkcje z pakietu do ogólnej przestrzeni nazw
print (factorial(6))
print (fibonacci(5))

#from rekurencja import factorial # uruchamianie funkcji działa tak samo, jak wyżej, ale importuje tylko jedną funkcję, a nie wszystkie z pakietu
#from rekurencja import fibonacci as fib

