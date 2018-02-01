def fibonacci_recursive(n):
    '''
    Recursively calculates the nth term in the Fibonacci sequence.
    :param n: an int representing the nth sequential value in the series
    :return: int
    '''

    if n > 2:
        return fibonacci_recursive(n-2) + fibonacci_recursive(n-1)
    return 1

def fibonacci_iterative(n):
    if n < 3:
        return(1)
    else:
        fib_2 = 1
        fib_1 = 1
        for i in range(2, n):
            value = fib_1 + fib_2
            print(float(value) / float(fib_2))
            fib_1 = fib_2
            fib_2 = value
        return(value)

print(fibonacci_iterative(30))
print(fibonacci_recursive(30))
