#!/usr/bin/env python3
"""

We are going to do this as test driven development. So your first task for each assignment below is to write a test that will ensure your code does what we are telling you it should do.

Keyword arguments:

    Write a function that has four optional parameters (with defaults):
        fore_color
        back_color
        link_color
        visited_color
    Have it return the colors (use strings for the colors)
    Call it with a couple different parameters set IOW, write tests that verify that all of the following work as advertised:
        using just positional arguments:
            func('red', 'blue', 'yellow', 'chartreuse')
        using just keyword arguments:
            func(link_color='red', back_color='blue')
        using a combination of positional and keyword
            func('purple', link_color='red', back_color='blue')
        using *some_tuple and/or **some_dict
            regular = ('red', 'blue')
            links = {'link_color': 'chartreuse'}
            func(*regular, *links)

Generic parameters:

    Write a new function with the parameters as:

*args and **kwargs

    Have it return the colors (use strings for the colors)
    Call it with the same various combinations of arguments used above.
    Also have it print args and kwargs directly, so you can be sure you understand what’s going on.
    Note that in general, you can’t know what will get passed into **kwargs So maybe adapt your function to be able to do something reasonable with any keywords.


"""

from args_kwargs import func

def test_01():
    assert func('red', 'blue', 'yellow', 'chartreuse') == ('red', 'blue', 'yellow', 'chartreuse')


def test_02():
    assert func(link_color='red', back_color='blue') == ('green', 'blue', 'red', 'maroon')

def test_03():
    assert func('purple', link_color='red', back_color='blue') == ('purple', 'blue', 'red', 'maroon')

def test_04():
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    assert func(*regular, **links) == ('red','blue','chartreuse', 'maroon')

    
