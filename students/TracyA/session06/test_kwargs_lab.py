#!/usr/bin/env python
import pytest

from kwargs_lab import colors, call_colors, colors_manual


# Programming in python B Winter 2018
# March 11, 2018
# Kwargs Tests
# Tracy Allen - git repo https://github.com/tenoverpar/Wi2018-Classroom


"""
Test code for the args-kwargs lab
"""
# Calling "colors" in various ways.


def test_all_positional():
    result = colors('red', 'blue', 'yellow', 'chartreuse')

    # this is not everything
    print(result)
    assert 'red' in result
    assert 'blue' in result
    assert 'chartreuse' in result


def test_one_keyword():
    result = colors(link_color='purple')
    # another attempt to test
    print(result)
    assert 'link:  purple' in result


def test_pos_and_keyword():
    result = colors('yellow', 'grey', link_color='purple')
    # not inclusive list
    print(result)
    assert 'foreground:  yellow' in result
    assert 'background:  grey' in result
    assert 'link:  purple' in result


def test_deplicate():
    """
    It's an error to a keyword arguments
    """
    # I am liking pytest more and more
    with pytest.raises(TypeError):
        result = colors('yellow', fore_color='purple')
        print(result)


def test_call_tuple():
    t = ('red', 'blue', 'yellow', 'chartreuse')
    result = colors(*t)
    print(result)
    assert 'red' in result
    assert 'blue' in result
    assert 'chartreuse' in result


def test_call_dict():
    d = {'fore_color': 'red',
         'visited_color': 'cyan',
         'link_color': 'green',
         'back_color': 'blue'}
    result = colors(**d)

    print(result)
    assert 'foreground:  red' in result
    assert 'background:  blue' in result
    assert 'link:  green' in result
    assert 'visited:  cyan' in result


def test_call_tuple_dict():
    t = ('red', 'blue')

    d = {'visited_color': 'cyan',
         'link_color': 'green'}

    result = colors(*t, **d)

    print(result)
    assert ' foreground:  red' in result
    assert 'background:  blue' in result
    assert 'visited:  cyan' in result
    assert 'link:  green' in result


def test_call_everything():
    t = ('red',)
    d = {'visited_color':  'cyan'}

    result = colors('blue', *t, link_color='orange', **d)
    print(result)
    assert 'foreground:  blue' in result
    assert 'background:  red' in result
    assert 'visited:  cyan' in result
    assert 'link:  orange' in result


def test_call_undefined_kwarg():
    with pytest.raises(TypeError):
        result = colors(wierd_color='grey')


def test_call_all_positional():
    args, kwargs = call_colors('red', 'blue', 'yellow', 'chartreuse')
    assert not kwargs
    assert args == ('red', 'blue', 'yellow', 'chartreuse')


def test_call_one_keyword():
    args, kwargs = call_colors(link_color='purple')

    assert not args
    assert kwargs['link_color'] == 'purple'
    assert len(kwargs) == 1


def test_call_pos_and_keyword():
    args, kwargs = call_colors('yellow', 'gray', link_color='purple')

    assert args == ('yellow', 'gray')
    assert kwargs == {'link_color': 'purple'}
