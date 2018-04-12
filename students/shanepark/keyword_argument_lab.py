def four_color(fore_color='red', back_color='blue', link_color='orange', visited_color='white'):
     ...:     return "{},{},{},{}".format(fore_color, back_color, link_color, visited_color)

red_white = ('red','white')
def four_color(fore_color='red', back_color='*red_white', link_color='orange', visited_color='white'):
     ...:     return "{},{},{},{}".format(fore_color, back_color, link_color, visited_color)

regular =  ('red', 'blue', 'purple')
def four_color(fore_color='red', back_color='*regular', link_color='orange', visited_color='white'):
     ...:     return "{},{},{},{}".format(fore_color, back_color, link_color, visited_color)

links= {'link_color':'chartreuse'}
 def four_color(fore_color='red', back_color='*regular', link_color='*links', visited_color='white'):
     ...:     return "{},{},{},{}".format(fore_color, back_color, link_color, visited_color)
     ...:

after asking to teacher:
def four_color(fore_color='red', back_color='blue', link_color='orange', visited_color='white'):
     ...:     return "{},{},{},{}".format(fore_color, back_color, link_color, visited_color)
     ...:

#In [146]: regular
#Out[146]: ('red', 'blue', 'purple')

#In [147]: four_color(*regular)
#Out[147]: 'red,blue,purple,white'

#In [148]: links
#Out[148]: {'link_color': 'chartreuse'}

#In [149]: four_color(**links)
#Out[149]: 'red,blue,chartreuse,white'


 def four_color(fore_color='red', *regular, visited_color='white', **links):
     ...:     return "{},{},{},{}".format(fore_color, regular, visited_color, links)

#In [161]: four_color('white', 'red', 'gray', 'pink', 'black', 'silver',links='hello')
#Out[161]: "white,('red', 'gray', 'pink', 'black', 'silver'),white,{'links': 'hello'}"
