#!/usr/local/bin/python3


"""
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/grid_printer.html#exercise-grid-printer

Write a function that draws a grid like the following:

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

"""

# grid 2x2
# Define the size of the cells
gridWidth=2
gridHeight=2

# Define number of rows and columns
gridRow=2
gridCol=2

def gridIsect(gridCol, gridWidth):
    """Draw the horizontal line to build up the intersection between the vertical rows"""

    # output just a single column (if more columns are needed continue below)
    if gridCol < 1:
        exit(0)   # exit if I don't have to print any columns

    print("+ ", end='')
    print("- " * gridWidth, end='')
    print("+", end='')

    if gridCol > 1:
        gridCol = gridCol - 1 # make it easy to assign variable number of colums, account for tricky + terminator on line
        loopControl = 0
        while loopControl < gridCol:
            print(" ", end='')
            print("- " * gridWidth, end='')
            print("+", end='')
            loopControl = loopControl + 1

    print() # Carriage return at the end of the line, because our "thing for building the rows" does not do this



def gridTall(gridHeight, gridWidth, gridCol):
    """Draw a horizontal line to build up the cell size for the height of the grid"""

    #if gridCol > 0:
    loopControl = 0
    rowControl = 0
    while rowControl < gridRow:
        while loopControl < gridHeight:
            i=0
            while i < gridCol:
                print("|", (" " * (2*gridWidth)), end='')
                i = i + 1

            if gridCol > 0:
                print("|") # terminate the line, but only if we acutually draw at least one row
            loopControl = loopControl + 1

        rowControl = rowControl + 1


def gridActual(gridRow, gridHeight, gridWidth, gridCol):
    """Assemble the grid from vertical gridTall bars and horizontal gridIntersections (gridIsect)

    gridRow = number of rows to draw
    gridCol = number of columns to draw

    gridWidth = width of columns to draw
    gridHeight = how tall to make the cells
    """

    z=0
    while z < gridRow:
        gridIsect(gridCol, gridWidth)
        gridTall(gridHeight, gridWidth, gridCol)

        z = z + 1

    gridIsect(gridCol, gridWidth)  # draw the bottom line on the grid


if __name__ == "__main__":
    gridActual(2, 8, 8, 2)
