#!/usr/local/bin/env python3

"""
Created By: Carol Farris
Fizz Buzz Excercise from Lesson 2 using if statements. 
I plan to review more sophistocated solutions and try to pull this back down, edit and resubmit. """

"""For each number 1-100 inclusive, print Fizz if it is a multiple of 3 and Buzz if multiple of 5.
Print FizzBuzz if number is a multiple of both 3 and 5"""
for i in range(1,101):
    if i%3 ==0 and i%5!=0:
        print("Fizz")
    elif i%5 == 0 and i%3!=0:
        print("Buzz")
    elif i%5==0 and i%3==0:
        print("FizzBuzz")
    else:
    	 print(i)    
