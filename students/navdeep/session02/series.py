def Fibonacci(n):
    """This method will recursively compute the
       Fibonacci Sequence.

       Args:
           n: the nth value of in the fibonacci sequence."""
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

def Lucas(n):
    """This method will recursively compute the
           Fibonacci Sequence.

           Args:
               n: the nth value of in the fibonacci sequence."""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return Lucas(n - 1) + Lucas(n - 2)

def PrintFib(n):
    """This function prints out the nth value of the Fibonacci series

       Args:
           n: the nth value of the fibonacci sequence."""
    print("The first " + str(n) + " integers in Fibonacci:")
    for i in range(n):
        print(Fibonacci(i), end = " ")
    print()

def PrintLucas(n):
    """This function prints out the nth value of the Lucas series

           Args:
               n: the nth value of the Lucas sequence."""
    print("The first " + str(n) + " integers of Lucas:")
    for i in range(n):
        print(Lucas(i), end = " ")
    print()

def sum_series(n1, n2, n3):
    """This method will recursively compute the
           Fibonacci Sequence or Lucas Sequence.

           Args:
            n1: the nth value of the fibonacci/lucas sequence.
            n2: optional parameter.
            n3: optional parameterce."""
    if n2 == 2 and n3 == 1:
        if n1 == 0:
            return 2
        elif n1 == 1:
            return 1
    else:
        if n1 == 0:
            return 0
        elif n1 == 1:
            return 1
    return sum_series(n1 - 1, n2, n3) + sum_series(n1 - 2, n2, n3)

def PrintSumSeries(n1, n2 = 0, n3 = 1):
    """This function prints out the nth value of the Fibonacci/Lucas series

           Args:
               n1: the nth value of the fibonacci/lucas sequence.
               n2: optional parameter.
               n3: optional parameter"""
    print("The first " + str(n1) + " integers in sequence:")
    for i in range(n1):
        print(sum_series(i, n2, n3), end=" ")
    print()

PrintFib(5)
PrintLucas(5)
PrintSumSeries(5)
PrintSumSeries(6, 2, 1)
