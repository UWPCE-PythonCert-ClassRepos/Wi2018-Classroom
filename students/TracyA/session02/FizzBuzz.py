#!/usr/bin/env python
# Programming in python B Winter 2018
# January 26, 2017
# FizzBuzz
# Tracy Allen - git repo https://github.com/tenoverpar/Wi2018-Classroom


for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
