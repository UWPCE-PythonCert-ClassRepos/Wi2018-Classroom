
import math as m
#------------------------------------------------------------------------
# Generators
#------------------------------------------------------------------------

def intsum(start=0):
    i = start
    a, b = start, start
    while True:
        a,b=a+b,i
        yield a+b
        i=i+1

def doubler(a=1):
    while True:
        yield a
        a = a + a

def fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

def square(a=1):
    b=1
    while True:
        yield a**2
        a,b=a+b,b+1


