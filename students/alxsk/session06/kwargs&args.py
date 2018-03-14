'''
Kwargs and Args exercise
Goal: Explore various ways to define and call functions
'''
#positional-or-keyword parameter with a default value
def color_param(fore_color = "red",back_color = "blue" ,link_color = "yellow", visited_color = "green"):
    print(fore_color,back_color,link_color,visited_color)
    return fore_color,back_color,link_color,visited_color

color_param()
print()

print("passing fore_color purple")
color_param(fore_color = "purple")
print()

#same thing as above in a string 
def string_color(fore_color = "red",back_color = "blue" ,link_color = "yellow", visited_color = "green"):
    print("passing color_param to into a string")
    str_color_param = "The color parameter are {fore_color} fore_color, {back_color} back_color, {link_color} link_color, and {visited_color} visited_color"

    str_color_param = str_color_param.format(fore_color = fore_color,
                                            back_color = back_color, 
                                            link_color = link_color,
                                            visited_color = visited_color)
    print(str_color_param)

string_color()


#Generalize paramters in a function using *args and **kwargs

def gen_parameter(*args, **kwargs):
    return args, kwargs


#Add tests here OR pass this file to a test file
#Call it with a couple different parameters set IOW, write tests that verify that all of the following work as advertised:
#using just positional arguments:
#func('red', 'blue', 'yellow', 'chartreuse')
#using just keyword arguments:
#func(link_color='red', back_color='blue')
#using a combination of positional and keyword
#``func('purple', link_color='red', back_color='blue')
#using *some_tuple and/or **some_dict
#regular = ('red', 'blue')
#links = {'link_color': 'chartreuse'}
#func(*regular, **links)
