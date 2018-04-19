

def make_row(char, middle = ' ', repeat = 4, length = 2):
    """create rows with "length" number of units and "repeat" size of units"""
    for k in range(length):
        print("%s%s" % (char, middle*repeat), end=' ')
    print(char)

#make_row('+', ' -')
#make_row('|', '  ')

def make_grid(length = 2, repeat = 4):
    """create grid with table height equal to length and cell height equal to repeat"""
    for k in range(length):
        make_row('+',' -', repeat, length)
        for j in range(repeat):
            make_row('|','  ',repeat, length)
    make_row('+',' -', repeat, length)

make_grid()
make_grid(3,4)
make_grid(5,3)