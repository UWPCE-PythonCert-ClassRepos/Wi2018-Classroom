


def fizzbuzz():
    """Write a program that prints the numbers from 1 to 100 inclusive.
But for multiples of three print “Fizz” instead of the number.
For the multiples of five print “Buzz” instead of the number.
For numbers which are multiples of both three and five print “FizzBuzz” instead."""
    checkersize = 100;
    for i in range(1,checkersize):
        if (i%3 == 0) and (i%7 == 0):
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%7 == 0:
            print("Buzz")
        else:
            print(i)
