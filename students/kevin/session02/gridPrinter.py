from itertools import repeat

def print_grid(n):

    # check that n is an odd int > 1
    if (n-1)%2 != 0 or n < 1:
        raise ValueError("Make sure 'n' is a positive odd integer")

    # get number of consecutive hyphens
    hyphens = int((n-1)/2)

    horLine = '+' + 2 * (hyphens * '-' + '+') + "\n"
    emptyLine = "|" + hyphens * " " + "|" + hyphens * " " + "|" + "\n"

    grid = horLine

    for _ in repeat(None, 2):
        for _ in repeat(None, hyphens):
            grid += emptyLine
        grid += horLine

    return grid

        
def print_grid2(c,n):

    # check that c is an odd int > 1 and that n is positive
    if n < 1 or (c-1)%2 != 0 or c < 1:
        raise ValueError("Make sure 'c' is a positive odd integer and 'n' is a positive integer")

    # get number of consecutive hyphens
    hyphens = n

    horLine = '+' + c * (hyphens * '-' + '+') + "\n"
    emptyLine = "|" + c * (hyphens * " " + "|") + "\n"

    grid = horLine

    for _ in repeat(None, c):
        for _ in repeat(None, hyphens):
            grid += emptyLine
        grid += horLine

    return grid
