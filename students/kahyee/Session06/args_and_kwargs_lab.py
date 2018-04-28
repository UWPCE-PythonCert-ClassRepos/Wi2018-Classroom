def func(fore_color="blue", back_color="red", link_color="yellow", visited_color="green"):
    return fore_color,back_color,link_color,visited_color

print(func('red', 'blue', 'yellow', 'chartreuse'))

print(func(link_color='red', back_color='blue'))

print(func('purple', link_color='red', back_color='blue'))

regular = ('red', 'blue')
links={'link_color': 'chartreuse'}
print(func(*regular, **links))


#Generic Parameters
def func2(*args, **kwargs):
    return (args, [item for key, item in kwargs.items()])

print(func2('red', 'blue', 'yellow', **links))
