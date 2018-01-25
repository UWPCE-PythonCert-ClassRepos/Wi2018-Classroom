#!/usr/local/bin/python3


"""
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/grid_printer.html#exercise-grid-printer

Write a function that draws a grid like the following:

+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +

Debug notes:
    still needs sizing work, prints out incorrect sizes, but prints a complete box
"""

# grid 2x2
gridWidth=2
gridHeight=2

def gridIsect():
    print("+", end='')
    print("-" * gridWidth, end='')
    print("+", end='')
    print("-" * gridWidth, end='')
    print("+") #grid terminate rightside


def gridTall():
    i=0
    while i < gridHeight:
        print("|", " " * (gridWidth - 2), "|", " " * (gridWidth - 2),"|")
        i = i + 1


def gridActual(numRow, numCol):

    closeRow = numRow + 1

    gridIsect()

    z=0
    while z < numRow:
        i=0
        while i < numCol:
            gridTall()
            i += 1
        gridIsect()

        z = z + 1




"""
    gridIsect()
    gridTall()
    gridIsect()
    gridTall()
    gridIsect()
"""

gridActual(gridWidth,gridHeight)
