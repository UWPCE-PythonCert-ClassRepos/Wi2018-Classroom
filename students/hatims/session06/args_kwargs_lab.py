#!/usr/bin/env python

"""
 function that has four optional parameters (with defaults
"""
def get_colors(fore_color = 'red', back_color = 'white', link_color = 'blue', visited_color = 'purple'):
    return fore_color, back_color, link_color, visited_color

def get_colors2(*args, **kwargs):
    return args, kwargs

	
regular = ('red', 'blue')
links = {'link_color': 'chartreuse'}

myarge = ['red', 'white']
mykwargs ={'link': 'blue', 'visited': 'purple'}
	
if __name__ == '__main__':
    assert get_colors() == ('red', 'white', 'blue', 'purple')
    assert get_colors(link_color='red', back_color='blue') == ('red', 'blue', 'red', 'purple')
    assert get_colors('purple', link_color='red', back_color='blue') == ('purple', 'blue', 'red', 'purple')
    assert get_colors(*regular, **links) ==('red', 'blue', 'chartreuse', 'purple')
    assert get_colors2(myarge, mykwargs) ==((['red', 'white'], {'link': 'blue', 'visited': 'purple'}), {})
    assert get_colors2('red', 'blue', 'yellow', 'chartreuse') == (('red', 'blue', 'yellow', 'chartreuse'), {})
    assert get_colors2(link_color='red', back_color='blue') == ((), {'link_color': 'red', 'back_color': 'blue'})