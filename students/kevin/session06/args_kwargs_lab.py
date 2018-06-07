#!/usr/bin/env python3

def colors_func(fore_color = "brown", back_color = "black",
                link_color = "green", visited_color = "cyan"):

    return fore_color, back_color, link_color, visited_color


def colors_ak_func(*args, **kwargs):


    print(f'args: {args}')
    print(f'kwargs: {kwargs}')
    
    return




def test_return_colors():
    assert colors_func('red', 'blue', 'yellow', 'chartreuse') == \
        ('red', 'blue', 'yellow', 'chartreuse')
    assert colors_func(link_color='red', back_color='blue') == \
        ('brown', 'blue', 'red', 'cyan')
    assert colors_func('purple', link_color='red', back_color='blue') == \
        ('purple', 'blue', 'red', 'cyan')

    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    assert colors_func(*regular, **links) == \
        ('red', 'blue', 'chartreuse', 'cyan')



if __name__ == '__main__':
    colors_ak_func('red', 'blue', 'yellow', 'chartreuse')
    colors_ak_func(link_color='red', back_color='blue')
    colors_ak_func('purple', link_color='red', back_color='blue')
    
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    colors_ak_func(*regular, **links)
