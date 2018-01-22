#!/usr/local/bin/python3

import sys


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


def altSyntaxError():
    """Alt Example to raise a type SyntaxError"""

    ### Note: uncomment for syntax error this does not even "compile"
    #### Maybe wrap in try except block and toss a continue later????

    ## altSyntaxError_ThisIsASyntaxError():

    return 0


def simpleAttributeError():
    """Example to raise a type AttributeError"""

    raise AttributeError('Raising a AttributeError')


def getValue():
    inputErrorNo=int(input('What type of error shall I create? \n1) NameError (raised) \n2) TypeError \n3) SyntaxError \n4) AttributeError \n5) NameError (actual) \nPlease enter a number for error type: '))
    return inputErrorNo



####
#### Main
####

try:
    inputErrorNoG=getValue()
except:
    inputErrorNoG=getValue()

    

if (inputErrorNoG == 1):
    print(inputErrorNoG)
    simpleNameError()
elif (inputErrorNoG == 2):
    print(inputErrorNoG)
    simpleTypeError()
elif (inputErrorNoG == 3):
    print(inputErrorNoG)
    simpleSyntaxError()
elif (inputErrorNoG == 4):
    print(inputErrorNoG)
    simpleAttributeError()
elif (inputErrorNoG == 5):
    print(inputErrorNoG)
    altNameError()
else:
    print('Not a valid choice for an error to create:', inputErrorNoG)


