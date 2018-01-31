#!/usr/local/bin/python3


"""

    https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/fib_and_lucas.html#exercise-fibonacci


    Create a new module series.py in the session02 folder in your student folder.
        In it, add a function called fibonacci.
        The function should have one parameter n.
        The function should return the nth value in the fibonacci series.
    Ensure that your function has a well-formed docstring



    ### Step 1

        Create a new module series.py in the session02 folder in your student folder.
            In it, add a function called fibonacci.
            The function should have one parameter n.
            The function should return the nth value in the fibonacci series.
        Ensure that your function has a well-formed docstring

    Note that the fibinacci series is naturally recursive – the value is defined by previous values:

    fib(n) = fib(n-2) + fib(n-1)


Lucas Numbers

The Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and 1. The resulting series looks like this:

2, 1, 3, 4, 7, 11, 18, 29, ...

In your series.py module, add a new function lucas that returns the nth value in the lucas numbers series (starting with zero index).

Ensure that your function has a well-formed docstring

"""


def fibonacci(n):
    """Return the nth value in the fibonacci series."""
    x=0
    y=1

    fibNumber=sumSeries(n, x, y)

    return fibNumber


def lucas(n):
    """Return the nth value in the lucas series."""
    x=2
    y=1

    lucasNumber=sumSeries(n, x, y)

    return lucasNumber


def sumSeries(n, x, y):
    """Return nth value in a given numbers series.

    Accomplish using array slicing, not by recursing the function from itself.


    test values:
    x=0
    y=1
    n="position in fibonacci"

    test values lucas:
    x=2
    x=1
    n="positin in lucas"

    localDebug=0 // if > 1 enable debugging, print additional output to screen

    """
    fibList = [x, y]
    fibVal=0
    localDebug=0

    for i in range(n):
        value = fibList[-2] + fibList[-1]
        fibList.append(value)

        if localDebug > 0:
            print(fibList)

        fibVal=fibList[-1]

    return fibVal



if __name__ == '__main__':
    print("Solution fibonacci: ", end='')
    print(fibonacci(4))

    print("Solution lucas: ", end='')
    print(lucas(4))
