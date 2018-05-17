#!/usr/bin/env python3
#factorial problem with recursion solution

def factorial(n):
   if n <1:   # base case
       return 1
   else:
       returnNumber = n * factorial(n - 1)  # recursive call
       print(f'{n}! = {returnNumber}')
       return returnNumber

def main():
    my_fact = factorial(5)
    my_fact2 = factorial(10)

if __name__ == '__main__':
    main()
