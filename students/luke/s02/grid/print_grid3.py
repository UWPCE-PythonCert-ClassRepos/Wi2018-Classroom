#!/usr/bin/env python3

"""
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/grid_printer.html#exercise-grid-printer

Write a function that draws a similar grid with a specified number of rows and columns, and with each cell a given size.

For example, print_grid2(3,4) results in:

+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
(three rows, three columns, and each grid cell four “units” in size)

What to do about rounding? – you decide.
"""

def print_edge(dimension, size):
    for i in range(dimension):
        print("+", end=' ')
        print(size * '- ', end='')
    print("+", end='')
    print()

def print_fill(dimension, size):
    for i in range(dimension):
        print("|", end=' ')
        print(size * '  ', end='')
    print("|", end='')
    print()

def print_grid(dimension, size):
    for j in range(dimension):
        print_edge(dimension, size)
        for i in range(size):
            print_fill(dimension, size)
    print_edge(dimension, size)

print_grid(3, 4)
print()
print_grid(5, 3)
