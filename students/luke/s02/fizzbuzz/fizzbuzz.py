#!/usr/bin/env python3

"""
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/fizz_buzz.html

Write a program that prints the numbers from 1 to 100 inclusive.
But for multiples of three print “Fizz” instead of the number.
For the multiples of five print “Buzz” instead of the number.
For numbers which are multiples of both three and five print “FizzBuzz” instead.
"""

def fizzbuzz(n):
    for i in range(1, n + 1):
        if (((i % 3) == 0) or ((i % 5) == 0)):
            if ((i % 3) == 0):
                print("Fizz", end='')
            if ((i % 5) == 0):
                print("Buzz", end='')
            print()
        else:
            print(i)

fizzbuzz(100)
