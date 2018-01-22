#!/usr/local/bin/python3

import sys


#raise new_exc from original_exc

#raise Exception

#raise ValueError('A very specific bad thing happened')



"""Explore Errors

    https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/python_pushups.html#python-pushups

    Add a new file to it called break_me.py

    In the break_me.py file write four simple Python functions:

    Each function, when called, should cause an exception to happen
    Each function should result in one of the four most common exceptions you’ll find.
    for review: NameError, TypeError, SyntaxError, AttributeError

    NameError, TypeError, SyntaxError, AttributeError
"""


def simpleNameError():
    """Example to raise a type NameError"""
    """Call an function with a value not defined"""

    raise NameError('Raising a NameError')

def altNameError():
    print(yourstuffisbroke)

def simpleTypeError():
    """Example to raise a type TypeError"""

    raise TypeError('Raising a TypeError')


def simpleSyntaxError():
    """Example to raise a type SyntaxError"""

    raise SyntaxError('Raising a SyntaxError')

def simpleAttributeError():
    """Example to raise a type AttributeError"""

    raise AttributeError('Raising a AttributeError')

def getValue():
    inputErrorNo=int(input('What type of error shall I create? \n1) NameError (raised) \n2) TypeError \n3) SyntaxError \n4) AttributeError \n5) NameError (actual) \nPlease enter a number for error type: '))
    return inputErrorNo


try:
    inputErrorNoG=getValue()
except:
    inputErrorNoG=getValue()

    

if (inputErrorNoG == 1):
   print(inputErrorNoG)
elif (inputErrorNoG == 2):
   print(inputErrorNoG)
elif (inputErrorNoG == 3):
   print(inputErrorNoG)
elif (inputErrorNoG == 4):
   print(inputErrorNoG)
elif (inputErrorNoG == 5):
   print(inputErrorNoG)
else:
   print('Not a valid choice for an error to create:', inputErrorNoG)



#print(inputErrorNo)


#tb = sys.exc_info()[2]
#raise OtherException(...).with_traceback(tb)
#raise OtherException(...).with_traceback(tb)
