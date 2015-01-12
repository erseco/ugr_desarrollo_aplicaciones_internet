#!/usr/bin/env python

L = [lambda x: x**2,
     lambda x: x**3]
     
for f in L:
   print (f(2))  # 4, 8