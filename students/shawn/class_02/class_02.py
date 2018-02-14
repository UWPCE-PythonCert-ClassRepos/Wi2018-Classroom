# Class 02 Exercises
def print_grid(cols, rows, width , height):

    """Grid Printer Exercise - Print a grid of cols x rows with cells width x height"""

    sep  = "+{}+".format("+".join(["-" * width for col in range(cols)]))
    body = "|{}|".format("|".join([" " * width for col in range(cols)]))

    for row in range(rows):
        is_sep = True
        for h in range(height+1):
            if is_sep:
                print(sep)
            else:
                print(body)
            is_sep = False

    print(sep)


print_grid(cols=4 , rows =4, width=4 , height=4)

#############################################################

# FizzBuzz - Summer asked to have it optionally work for a single value

def assign_status(val):

    """Return fizbuzz for a single int"""

    is_fiz = val % 3 == False
    is_buz = val % 5 == False

    if (is_buz * is_fiz):
        return "FizzBuzz"
    elif is_fiz and not is_buz:
        return "Fizz"
    elif  is_buz and not is_fiz:
        return "Buzz"
    else:
        return val


def fizz_buzz(val):

    """Fizz Buzz Exercise  - display fizzbuzz for list or int"""

    if type(val)is list:
        for i in range(val[0],val[1]):
            print(assign_status(i))
    else:
        print(assign_status(val))

fizz_buzz(15)



#############################################################

from enum import Enum

# Add enum switch to use fibonacci or lucas
class Series(Enum):
    Fibonacci = 1
    Lucas = 2

# Func to format the nth value in english
def ordinal(val):

    try:
        return f"{val}{['st','nd','rd'][val-1]}"
    except IndexError:
        return f"{val}th"

def fib_luc(nth, series = Series.Lucas ):

    """Return the nth number of either the Lucas or Fibonacci series"""

    start_point = [0,1] if series == Series.Fibonacci else [2,1]
    for i in range(2,nth):
        val=start_point[i-2] + start_point[i-1]
        start_point.append(val)

    print(f"The {ordinal(nth)} {series.name} number is {start_point[-1]}")


fib_luc(3,series=Series.Fibonacci)
fib_luc(13,series = Series.Lucas)
