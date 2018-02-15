#!/usr/bin/env python
# Programming in python B Winter 2018
# January 27, 2017
# Grid printer
# Tracy Allen - git repo https://github.com/tenoverpar/Wi2018-Classroom


def new_grid(a=3, b=4):
    """This is my doc string for a Grid"""
    border = '+' + b * (' ' + '-' + ' ')
    body = '|' + b * 3 * (' ')
    for i in range(a):
        print(a * border + '+')
        for i in range(b):
            print(body * a + '|')
    print(a * border + '+')


new_grid()
