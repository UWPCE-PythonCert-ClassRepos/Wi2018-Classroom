def print_columns():
    line_b = "|         |         |"
    for i in range(3):
        print(line_b)

def gridprint():
    line_a = "+ - - - - + - - - - +"
    print(line_a)
    print_columns()
    print(line_a)
    print_columns()
    print(line_a)

gridprint()

