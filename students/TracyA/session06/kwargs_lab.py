#!/usr/bin/env python
from collections import OrderedDict


# Programming in python B Winter 2018
# March 11, 2018
# Kwargs lab
# Tracy Allen - git repo https://github.com/tenoverpar/Wi2018-Classroom


"""
call_colors() is a function that takes totaly generic arguments
the test code calls it in various ways so you can confirm it works as expected.

colors_manual() takes generic arguments, but processes it as if it
  had keyworkd parameters.
"""


def colors(fore_color='red',
           back_color='blue',
           link_color='green',
           visited_color='cyan'):

    output = ("The colors are: \n"
              "    foreground:  {fore_color}\n"
              "    background:  {back_color}\n"
              "    link:  {link_color}\n"
              "    visited:  {visited_color}")
    output = output.format(fore_color=fore_color,
                           back_color=back_color,
                           link_color=link_color,
                           visited_color=visited_color)

    return output


def call_colors(*args, **kwargs):
    """
    So this function will simpily return args and kwargs, and the test.

    *args and **kwargs should be saved for times when you NEED generic
    function processing.
    """
    return args, kwargs


def colors_manual(*args, **kwargs):
    """
    This example to show you how much work you need to do to do this by hand!

    """
    default_colors = OrderedDict((('fore_color', 'red'),
                                  ('back_color', 'blue'),
                                  ('link_color', 'green'),
                                  ('visited_color', 'cyan')))

    for key in kwargs:
        if key not in default_colors:
            msg = "colors_manual() got an expcted keyword argument: {}".format(key)
            raise TypeError

    all_args = {}
    # uppacking now
    for i, key in enumerate(default_colors.keys()):
        try:
            all_args[key] = args[i]
        except IndexError:
            break

    for key, color in default_colors.items():
        if key in all_args:
            if key in kwargs:
                msg = "colors_manual() go mult values for argument '{}'".format(key)
                raise TypeError(msg)
            elif key in kwargs:
                # from the dictionary
                all_args[key] = kwargs[key]
            else:
                all_args[key] = color

    output = ("The colors are:\n"
              "  foreground: {fore_color}\n"
              "  back_color: {back_color}\n"
              "  link:  {link_color}\n"
              "  visited:  {visited_color}")
    output = output.format(**all_args)

    return output
