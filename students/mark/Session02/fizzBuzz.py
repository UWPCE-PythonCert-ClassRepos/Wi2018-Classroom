#!/usr/bin/env python3

"""
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/fizz_buzz.html


    Write a program that prints the numbers from 1 to 100 inclusive.
    But for multiples of three print Fizz instead of the number.
    For the multiples of five print Buzz instead of the number.
    For numbers which are multiples of both three and five print FizzBuzz instead.


"""

for i in range(1,16):
    if ((i % 3) == 0) and ((i % 5) == 0):
        print("FizzBuzz")
    else:
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
