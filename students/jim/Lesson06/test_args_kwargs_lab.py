from args_kwargs_lab import color_function

def test_1():
    assert color_function('red', 'green', 'mauve', 'yellow') ==\
    ('red', 'green', 'mauve', 'yellow')


def test_2():
    assert color_function(link_color='orange', back_color='gray') ==\
    ('white', 'gray', 'orange', 'purple')


def test_3():
    assert color_function('pink', visited_color='green') ==\
    ('pink', 'black', 'blue', 'green')


def test_4():
    regular = ('red', 'blue')
    links = {'link_color':'teal', 'visited_color':'brown'}
    assert color_function(*regular, **links) ==\
    ('red', 'blue', 'teal', 'brown')
