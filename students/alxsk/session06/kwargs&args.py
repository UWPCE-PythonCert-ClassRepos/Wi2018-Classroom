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

def string_color(fore_color = "red",back_color = "blue" ,link_color = "yellow", visited_color = "green"):
    print("passing color_param to into a string")
    str_color_param = "The color parameter are {fore_color} fore_color, {back_color} back_color, {link_color} link_color, and {visited_color} visited_color"

    str_color_param = str_color_param.format(fore_color = fore_color,
                                            back_color = back_color, 
                                            link_color = link_color,
                                            visited_color = visited_color)
    print(str_color_param)

string_color()



