#!/usr/bin/env python3

"""
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/grid_printer.html#exercise-grid-printer:

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
"""

def print_grid():
    for i in range(1, 12):
        for j in range(1, 12):
            if ((i % 5) == 1):
                if ((j % 5) == 1):
                    print('+', end=' ')
                else:
                    print('-', end=' ')
            else:
                if ((j % 5) == 1):
                    print('|', end=' ')
                else:
                    print(' ', end=' ')
        print()

print_grid()
