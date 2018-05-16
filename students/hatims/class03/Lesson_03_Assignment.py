#!/usr/bin/env python

def factorial( n ):
   if n <1:   
       return 1
   else:
       temp = factorial( n - 1)
       print("{}!".format(n-1), temp)
       return n * temp