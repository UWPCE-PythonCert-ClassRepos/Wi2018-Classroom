def fibonacci(n):
    '''
    Recursively calculates the nth term in the Fibonacci sequence.
    :param n: an int representing the nth sequential value in the series
    :return: int
    '''

    if n > 2:
        return fibonacci(n-2) + fibonacci(n-1)
    return 1

print(fibonacci(10))