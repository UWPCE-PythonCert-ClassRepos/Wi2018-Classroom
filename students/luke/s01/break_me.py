#!/usr/bin/env python3

# https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/python_pushups.html#python-pushups
#
# In the break_me.py file write four simple Python functions:
#
# Each function, when called, should cause an exception to happen
# Each function should result in one of the four most common exceptions
# you’ll find.
# for review: NameError, TypeError, SyntaxError, AttributeError

import random, sys

def throw_NameError():
    raise NameError()

def throw_TypeError():
    raise TypeError()

def throw_SyntaxError():
    raise SyntaxError()

def throw_AttributeError():
    raise AttributeError()

def throw_Exception():
    rval = random.randint(0, 3)

    if (rval == 0): throw_NameError()
    elif (rval == 1): throw_TypeError()
    elif (rval == 2): throw_SyntaxError()
    elif (rval == 3): throw_AttributeError()
    else:
        print("Bad switch value.")
        raise RuntimeError()

def main():
    random.seed()

    try:
        throw_Exception()
    except Exception as e:
        print("Caught exception", type(e).__name__)
        raise e
    else:
        print("No exception thrown.")
    finally:
        print("Done.")

if __name__ == "__main__":
    main()
