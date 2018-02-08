def fibonacci(n):
    """ Returns the nth value of the Fibonacci sequence by recursion """
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    elif (n > 1):
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        return None

def lucas(n):
    """ Returns the nth value of the Lucas sequence by recursion """
    if (n == 0):
        return 2
    elif (n == 1):
        return 1
    elif (n > 1):
        return lucas(n-1) + lucas(n-2)
    else:
        return None

def sum_series(n, n1=0, n2=1):
    """ Returns the nth value of a Fibonacci-like sequence (given
    the first two values in the series) by recursion """
    if (n == 0):
        return n1
    elif (n == 1):
        return n2
    elif (n > 1):
        return sum_series(n-1, n1, n2) + sum_series(n-2, n1, n2)
    else:
        return None

print("Fibonacci")
for i in range(0, 10):
    print(i, fibonacci(i))

print("Lucas:")
for i in range(0, 10):
    print(i, lucas(i))

print("Sum_Series Fibonacci:")
for i in range(0, 10):
    print(i, sum_series(i))

print("Sum_Series Lucas:")
for i in range(0, 10):
    print(i, sum_series(i, 2, 1))
