from math import floor

def makingABox():
    """This is a function that makes a grid"""
    filledline = '+ - - - - + - - - - +'
    emptyline = '|         |         |'
    print(filledline)
    print(emptyline)
    print(emptyline)
    print(emptyline)
    print(emptyline)
    print(filledline)
    print(emptyline)
    print(emptyline)
    print(emptyline)
    print(emptyline)
    print(filledline)

def boxOfSetSize(boxsize):
    """This is a function that makes a 2x2 grid - user must specify size"""
    halfsize = floor(boxsize/2)
    filledline = '+ '+'- '*halfsize+'+ '+'- '*halfsize+'+'
    emptyline = '| ' + '  ' * halfsize + '| ' + '  ' * halfsize + '|'
    print(filledline)
    for i in range(halfsize):
        print(emptyline)
    print(filledline)
    for i in range(halfsize):
        print(emptyline)
    print(filledline)

def boxOfTwoParameters(gridsize,boxsize):
    """This is a function that makes a grid - inputs are number of boxes per row/col, and size of box"""
    filledline = ('+ '+'- '*boxsize)*gridsize+'+'
    emptyline = ('| '+'  '*boxsize)*gridsize+'|'

    for i in range(gridsize):
        print(filledline)
        for i in range(boxsize):
            print(emptyline)
    print(filledline)

