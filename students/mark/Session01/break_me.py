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


def altTypeError():
    """Example to raise a type TypeError"""

    notANumber = "1"
    total = notANumber + 3 

    return total


def simpleSyntaxError():
    """Example to raise a type SyntaxError"""

    raise SyntaxError('Raising a SyntaxError')


def altSyntaxError():
    """Alt Example to raise a type SyntaxError"""

    ### Note: uncomment for syntax error this does not even "compile"


    ## altSyntaxError_ThisIsASyntaxError():

    """
     Thoughts and options:
     Maybe wrap in try except block and toss a continue later????
     Nope, that fails on "compile" too.
     There has got to be an easier way: https://docs.python.org/3/library/warnings.html
     The python3 interpreter is really good at letting you know there is a sytnax error.
    """

    try:
        ## altSyntaxError_ThisIsASyntaxError():
        print('This error type does not actual "compile"')
        print("Instead the output of the failure is provided as an example: \n\n")
        formattedText="""
              File "./break_me.py", line 71
                altSyntaxError_ThisIsASyntaxError():
                                                   ^
            SyntaxError: invalid syntax"""

        print('  File "./break_me.py", line 71')
        print("    altSyntaxError_ThisIsASyntaxError():")
        print("                                             ^")
        print("SyntaxError: invalid syntax ")
        print()
    except:
        print("altSyntaxError: ", e)

    return 0


def simpleAttributeError():
    """Example to raise a type AttributeError"""

    raise AttributeError('Raising a AttributeError')

def altAttributeError():
    """create an attribute error """

    """Created by attempting to use an attribute which does not exist for the datatype"""
    a="sometext"
    a.append["somejunktext"]

    return 0


def noErrorsPlease():
    """Exit without errors"""

    return 0


def getValue():
    inputErrorNo=int(input('What type of error shall I create? \n1) NameError (raised) \n2) TypeError \n3) SyntaxError \n4) AttributeError \n5) NameError (actual) \n6) TypeError (actual) \n7) SyntaxError (actual) \n8) AttributeError (actual) \n9) Exit without an error. \nPlease enter a number for error type: '))
    return inputErrorNo



####
#### Main
####


try:
    """Catch the error if the value is not correctly entered and reprompt the user"""
    """Collects garbage input like $"""
    inputErrorNoG=getValue()
except:
    inputErrorNoG=getValue()

    
"""Call the function to create the error"""

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
elif (inputErrorNoG == 6):
    print(inputErrorNoG)
    altTypeError()
elif (inputErrorNoG == 7):
    print(inputErrorNoG)
    altSyntaxError()
elif (inputErrorNoG == 8):
    print(inputErrorNoG)
    altAttributeError()
elif (inputErrorNoG == 9):
    print(inputErrorNoG)
    noErrorsPlease()
else:
    print('Not a valid choice for an error to create:', inputErrorNoG)


