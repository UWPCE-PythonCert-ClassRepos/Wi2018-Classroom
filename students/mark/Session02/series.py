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


"""

def recurseMeSimple(n):
    """Simple example of recursion (works)"""

    n = n + 1

    if n > 15:
        return(15)

    print(n)
    recurseMeSimple(n)

    return n


def basicFibonacci(a,b):
    """The Fibonacci Series is a numeric series starting with the integers 0 and 1.

    In this series, the next integer is determined by summing the previous two.

    This gives us:

    0, 1, 1, 2, 3, 5, 8, 13, ...

    (returns a few fibonacci numbers)
    (works)
    """

    #a=0
    #b=1

    #0 = 0 + 0
    #1 = 0 + 1
    #2 = 1 + 1
    #3 = 1 + 2
    #5 = 2 + 3
    #8  = 3 + 5
    #13 = 5 + 8

    fib = a + b
    #print('fib: ', fib)

    if b > 988:
        return

    fib=basicFibonacci(b,fib)

    print(fib)

    return(fib)


def fibonacciLoop(loopNumber):
    """This function is a Work in Progress on creating a fibonncaai number in a loop"""

    """create a fibonacci which computes the nth postion integer"""

    """return 2 val, number of times through loop; number of times called"""
    a=0
    b=1
    fibOld=a
    fib = a + b

    print(a)
    print(b)
    print(fib)

    fib=basicFibonacci(a,b)
    b=fib
    a=b
    exit(32)

    print("a: ", a)
    print("b: ", b)
    print("fib: ", fib)


    if b > 500000:
        return

    ##fibArr=[]
    ##fib=basicFibonacci(fibOld,fib)
    #fibArr.append(fib)

    print(fib)

    # for i in fibArr:
    #     print("i: ", "fibNumber: ", fibArr[i])

    return(fib)



fib=0
def fibonacciOneInput(n):
    """this function is a work in progress to return an nth value w/o a dict"""
    """Return the nth value in the fibonacci series"""

    ##fib = fibonacci(n-2) + fibonacci(n-1)
    #fib_runner(fnum-1)+fib_runner(fnum-2)
    fib=15

    print(fib)
    fib=fibonacci(n-1)+fibonacci(n-2)
    n = n + 1
    #fib = (n - 2) + (n - 1)
    print(fib)


    return fib


previous = {0:0, 1:1}
def fibonacci(n):
    """approved green tea press answer (modified for python3 (has_key, using get))"""
    #define out side function: previous = {0:1, 1:1}
    #if previous.get(n):
    if n in previous:
        return previous[n]
    else:
        newValue = fibonacci(n-1) + fibonacci(n-2)
        previous[n] = newValue

    return newValue


known = {0:0, 1:1}
def fibonacciKnown(n):
    """aproved green tea press answer
    http://greenteapress.com/thinkpython2/html/thinkpython2012.html#sec134 """
    if n in known:
        return known[n]

    res = fibonacciKnown(n-1) + fibonacciKnown(n-2)
    known[n] = res
    return res


if __name__ == '__main__':
    print("demonstrate recursion: ")
    recurseMeSimple(0)

    print("greenTeaAnswer Example (fibonacci): ", end="")
    print(fibonacci(4))

    print("greenTeaAnswer Python3 Example (fibonacci): ", end="")
    print(fibonacciKnown(4))

#recurseMeSimple(0)
print('###')
#basicFibonacci(0,1)
print('###')
fibonacciLoop(13)
print('###')
fibonacciOneInput(8)

"""
Student Notes: Not exactly sure how we're supposed to accomplish recursing a fibonnicci set with a single input var,
no lookup table(dictonary) and using only the info in ThinkPython2(ch1-6)??
http://greenteapress.com/thinkpython2/html/thinkpython2007.html




#####
#####
#####
##### Instructions from web page:
##### https://uwpce-pythoncert.github.io/PythonCertDevel/class_schedule/session_1_02.html#session-1-02
Session 2: Basic Python and Functions

Basic Python and Functions
Pre-class prep
Dev environment

Make sure you know how to create a python file, save it, edit it, run it, etc.

Also make sure you are comfortable “playing” with python in the iPython command line.

If you are uncomfortable with the command line, brush up on that: This: is a good tutorial.
Python
Python Tutorial

Tutorials come in many forms, but I define a python “tutorial” as a quick high-level introduction, designed to kick start your python programming. It should give you enough to get something done, but not provide a lot of detailed explanations. If you have been doing a bit of python coding already, or have taken an introductory programing class with Python, then you may be able to skip this step.

Every one of you has a different background and learning style. So take a bit of time to figure out which resource works for you.

Useful Python Learning Resources

Provides some options. Do look it over.
Python Basics

If you are comfortable with the materials in a tutorial, it’s time for some more in-depth discussion. Here are a few options to get you started this week:

Finish Reading: Basic Python

Read: More on Functions

Read: Documentation
Supplimental Reading

If that is too fast, then here are some good options for another look:

Think Python: Chapters 1–6 (http://greenteapress.com/thinkpython2/html/index.html)

Dive Into Python: Chapters 1–2 (http://www.diveintopython3.net/)

LPTHW: ex. 1–10, 18-21 (https://learnpythonthehardway.org/python3/)

(note: LPTHW used to be totally free –now it looks like you may only get a sneak peak – darn! – but the first few “chapters” are available)

GOAL

You should be comfortable with working with variables, numbers, strings, and basic functions before we start class next week.
git

We are only using a small subset of git functionality for this class, but if you feel lost, and/or want to know more, these are some good resources:

http://rogerdudler.github.io/git-guide/

or

https://try.github.io/
In-class Activities

Review Python Pushups
Exercises:

Grid Printer Exercise

Fizz Buzz Exercise

Fibonacci Series Exercise
Post-class Activities

Finish the Exercises

Look at the next session for reading, etc:

Session 3: Booleans, Sequences, Iteration, and Strings

"""
