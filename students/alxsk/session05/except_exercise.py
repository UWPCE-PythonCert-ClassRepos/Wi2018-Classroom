#!/usr/bin/python

"""
An exercise in playing with Exceptions.
Make lots of try/except blocks for fun and profit.

Make sure to catch specifically the error you find, rather than all errors.
"""

from except_test import fun, more_fun, last_fun


first_try = ['spam', 'cheese', 'mr death']
langs = ['java', 'c', 'python']

try:
    joke = fun(first_try[0])

   # not_joke = fun(first_try[2])
    #print(not_joke)
except NameError:
    try:
        joke = fun(first_try[1])
    except SyntaxError:
        print('Run Away!')
    else: 
        not_joke = fun(first_try[2])
        print(not_joke)

try: 
    next_joke = more_fun(langs[1])
except SyntaxError:
        print('Run Away!')
else:
    more_fun(langs[2])
finally:
    last_fun()
