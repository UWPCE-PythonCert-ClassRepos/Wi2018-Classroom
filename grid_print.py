corner = ' +'
horiz_char = ' -'
vert_char = ' |'
space = '  '


def print_grid(cell_size, grid_size):
    vert_line = ""
    horiz_line = ""

    for x in range(cell_size):
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


print_grid(3, 3)