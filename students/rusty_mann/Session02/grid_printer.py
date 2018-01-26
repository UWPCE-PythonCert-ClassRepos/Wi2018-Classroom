

def make_row(char, middle = ' ', repeat = 2, length = 2):
    """create rows with "length" number of units and "repeat" size of units"""
    for k in range(length):
        print("%s%s" % (char, middle*repeat), end=' ')
    print(char)

make_row('+', ' -')
make_row('|', '  ')
