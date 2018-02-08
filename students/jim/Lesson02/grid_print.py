corner = ' +'
horiz_char = ' -'
vert_char = ' |'
space = '  '


def print_grid(cell_size, grid_size):
    '''
    Prints a grid with dimensions controlled by input
    :param cell_size: dimensions of each cell (more or less...)
    :param grid_size: dimensions of (square) grid
    :return: void
    '''

    horiz_line = ""
    vert_line = ""

    for x in range(grid_size):
        horiz_line += (corner + ((cell_size-1)*horiz_char))
        vert_line += (vert_char + ((cell_size-1)*space))
    horiz_line += corner
    vert_line += vert_char

    for y in range(grid_size * cell_size):
        if y % cell_size == 0:
            print(horiz_line)
        else:
            print(vert_line)

    print(horiz_line)


print_grid(2, 2)