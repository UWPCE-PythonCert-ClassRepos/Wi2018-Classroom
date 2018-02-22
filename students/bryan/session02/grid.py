def print_columns():
    line_b = "|         |         |"
    for i in range(3):
        print(line_b)

def gridprint():
    """print the grid. simpler version with no arguments"""
    line_a = "+ - - - - + - - - - +"
    print(line_a)
    print_columns()
    print(line_a)
    print_columns()
    print(line_a)

def gridprint2(rows=2, columns=2, cell_size=4):
    """print a grid using the arguments"""
    line_a = ("+" + cell_size * " - ") * columns + "+" #make horizontal lines
    line_b = ("|" + cell_size * "   ") * columns + "|" #make fodder for vertical lines

    filler = ""
    for i in range(cell_size): #make vertical lines
        filler += (line_b + "\n")
    filler = filler.rstrip()

    for i in range(rows): #print the grid
        print(line_a)
        print(filler)
    print(line_a)
    #print(line_a)
    #print(line_b)

gridprint2(4,14,2)
#gridprint()

