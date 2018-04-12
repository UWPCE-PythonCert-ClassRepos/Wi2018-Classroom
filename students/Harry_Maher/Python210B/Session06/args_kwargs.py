#!/usr/bin/env python3
"""

Procedure

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
            ``func('purple', link_color='red', back_color='blue')
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

def func(fore_color="green", back_color="white", link_color="blue", visited_color="maroon"):
    return fore_color, back_color, link_color, visited_color

# I'm sort of confused and don't know if I'm supposed to do anything more than this.
# If I don't have defaults this will return different values than func?
# Unless I'm supposed to write more?
def func2(*args, **kwargs):
    print("args:",args)
    print("kwargs:",kwargs)
    return args, kwargs

func2('red', 'blue', 'yellow', 'chartreuse')
func2(link_color='red', back_color='blue')
func2('purple', link_color='red', back_color='blue')
regular = ('red', 'blue')
links = {'link_color': 'chartreuse'}
func2(*regular, **links)