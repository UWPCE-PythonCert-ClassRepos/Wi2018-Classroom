"""
Goal:

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


#A very lazy gridprinter...
def gridprinter(size):
    n = size//2
    print("+"+(" -"*n+" +"+(" -"*n+" +")))
    for i in range(n):
        print("|"+"  "*n+" |"+"  "*n+" |")
    print("+"+(" -"*n+" +"+(" -"*n+" +")))
    for i in range(n):
        print("|"+"  "*n+" |"+"  "*n+" |")
    print("+"+(" -"*n+" +"+(" -"*n+" +")))


def gridprinter2(rows,size):
    """Prints a grid with specified number of rows and size"""
    column_b = ("+ "+"- "*size)*rows + "+"
    column = ("| " + "  "*size)*rows + "|"
    for i in range(rows):
        print(column_b)
        for i in range(size):
            print(column)
    print(column_b)

#gridprinter(10)
#gridprinter2(10,2)
#help(gridprinter2)

"""

    Write a program that prints the numbers from 1 to 100 inclusive.
    But for multiples of three print “Fizz” instead of the number.
    For the multiples of five print “Buzz” instead of the number.
    For numbers which are multiples of both three and five print “FizzBuzz” instead.
"""
def fizzbuzz(r = 101):
    for i in range(r):
        pr = ""
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)
#fizzbuzz()