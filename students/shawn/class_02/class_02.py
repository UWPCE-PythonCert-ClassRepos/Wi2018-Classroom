# Class 02 Exercises
def print_grid(cols=2, rows=2, width=5, height=5):
    """Grid Printer Exercise - Print a grid of cols x rows with cells width x height"""
    sline = [] #separator line
    bline = [] #body line
    sep = ""
    body = ""
    for col in range(cols):
        sline.append("-" * width)
        sep="+{}+".format("+".join(sline))
        bline.append(" " * width)
        body="|{}|".format("|".join(bline))

    for row in range(rows):
        is_sep = True
        for h in range(height):
            if is_sep:
                print(sep)
            else:
                print(body)
            is_sep = False

    print(sep)


print_grid(cols  = 5 , rows = 5 , width = 5 , height = 5)

#############################################################

def fizz_buzz():
    """Fizz Buzz Exercise"""
    for i in range(1,100):
        is_fiz = i%3==False
        is_buz = i%5==False

        if (is_fiz and is_buz):
            print("FizzBuzz")
        elif is_fiz:
            print("Fizz")
        elif is_buz:
            print("Buzz")
        else:
            print (i)

fizz_buzz()

#############################################################

from enum import Enum

# Instead of redundant functions, add series type as keyword enum to remove ambiguity
class Series(Enum):
    Fibonacci = 1
    Lucas = 2

def fib_luc(nth, series = Series.Lucas ):

    """Return the nth number of either the Lucas or Fibonacci series"""

    start_point=[0,1] if series == Series.Fibonacci else [2,1]
    for i in range(2,nth):
        val=start_point[i-2] + start_point[i-1]
        start_point.append(val)

    print("{} number =  {}".format(series.name,start_point[-1]))

fib_luc(15,series = Series.Fibonacci)
fib_luc(15,series = Series.Lucas)
