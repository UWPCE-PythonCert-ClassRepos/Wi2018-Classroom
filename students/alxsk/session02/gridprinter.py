'''Grid printer exercise
A series of increasingly complex functions to create grids
'''
from textwrap import dedent 

# 1. Printing a basic grid
print(dedent('''
    + - - - - + - - - - +
    |         |         |
    |         |         |   
    |         |         |   
    |         |         |   
    + - - - - + - - - - +
    |         |         |   
    |         |         |   
    |         |         |   
    |         |         | 
    + - - - - + - - - - + 
    '''))

# 2. Generalize the fill of the above grid into a function

print('A function that changes the size of the grid.')
def print_grid(number):
    number_of_units=int(number)
    horizontal = '+ ' + (number*'- ') + '+ ' + (number*'- ') + '+' + '\n'
    filler = '| ' + (number* '  ') + '| '+ (number* '  ') + '|'+'\n'
    vertical= filler*number

    grid = horizontal + vertical + horizontal + vertical + horizontal
   
    print(grid)

size= int(input('Size of grid: '))
print(print_grid(size))

#3. Generalize the number of boxes and the fill
print('A function that changes the size of grid and number of boxes')

def print_grid_2(number, boxes):
    number_of_units=int(number)
    horizontal = ('+ ' + (number*'- ')) * boxes + '+' + '\n'
    filler = ('| ' + (number* '  ') )*boxes + '|'+'\n'
    vertical= filler*number

    grid = (horizontal + vertical)*boxes + horizontal
   
    print(grid)    

fill = int(input('Size of grid: '))
boxes = int(input('Number of boxes: '))
print(print_grid_2(fill, boxes))