#!/usr/bin/env python3

"""
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/grid_printer.html#exercise-grid-printer

Write a function print_grid(n) that takes one integer argument and prints a grid just like before, BUT the size of the grid is given by the argument.

For example, print_grid(11) prints the grid in the above picture.

print_grid(3) would print a smaller grid:

+ - + - +
|   |   |
+ - + - +
|   |   |
+ - + - +
"""
def print_edge(n):
    print("+", end=' ')
    print((n//2 - 1) * '- ', end='')
    print("+", end=' ')
    print((n//2 - 1) * '- ', end='')
    print("+", end='')
    print()

def print_fill(n):
    print("|", end=' ')
    print((n//2 - 1) * '  ', end='')
    print("|", end=' ')
    print((n//2 - 1) * '  ', end='')
    print("|", end='')
    print()

def print_grid(n):
    print_edge(n)
    for i in range(0, n//2 - 1):
        print_fill(n)
    print_edge(n)
    for i in range(0, n//2 - 1):
        print_fill(n)
    print_edge(n)

print_grid(3)
print()
print()
print_grid(5)
print()
print()
print_grid(7)
print()
print()
print_grid(9)
print()
print()
