#!/usr/bin/env python

"""
def colors(fore_color="blue",back_color="red",link_color="yellow",visited_color="green"):
    return fore_color,back_color,link_color,visited_color

"""


from args_kwargs import args_kwargs



def test_1():
    assert colors('red', 'blue', 'yellow', 'chartreuse') == ('red', 'blue', 'yellow', 'chartreuse')


def test_2():
    assert colors(link_color='red', back_color='blue') == ('blue', 'blue', 'red', 'green')