#!/usr/bin/env python3


def fibonacci(n):
    """ Return the nth number in the fibonacci sequence. """

    fib_n0 = 0
    fib_n1 = 1

    iterations = (n - 1) / 2
    
    while iterations > 0:
        fib_n0 = fib_n0 + fib_n1
        fib_n1 = fib_n0 + fib_n1

        iterations-=1

    fibs = list((fib_n0, fib_n1))
    relative_n = n % 2  # nth number in series relative to number of iterations

    return fibs[relative_n]


def lucas(n):
    """ Return the nth number in the lucas sequence. """

    luc_n0 = 2
    luc_n1 = 1

    iterations = (n - 1) / 2

    while iterations > 0:
        luc_n0 = luc_n0 + luc_n1
        luc_n1 = luc_n0 + luc_n1

        iterations-=1

    lucs = list((luc_n0, luc_n1))
    relative_n = n % 2  # nth number in series relative to number of iterations

    return lucs[relative_n]


def sum_series(n, n0=0, n1=1):
    """
    Return the nth number in a summation series.
    
    :param n0: value of zeroth element in the series
    :param n1: value of the first element in the series
    
    if n0 == 0 and n1 == 1, the result is the Fibbonacci series

    if n0 == 2 and n1 == 1, the result is the Lucas series
    """

    iterations = (n - 1) / 2

    while iterations > 0:
        n0 = n0 + n1
        n1 = n0 + n1

        iterations-=1

    ns = list((n0, n1))
    relative_n = n % 2  # nth number in series relative to number of iterations

    return ns[relative_n]


if __name__ == '__main__':
    # Run some tests.
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(0) == 2
    assert lucas(1) == 1

    assert lucas(4) == 7

    assert sum_series(5) == fibonacci(5)

    # Test if sum_series matched lucas.
    assert sum_series(5, 2, 1) == lucas(5)

    # My own tests
    assert fibonacci(7) == 13, "The 8th value in the Fibonacci sequence should be 13"
    assert lucas(7) == 29, "The 13th value in the Fibonacci sequence should be 29"
    assert sum_series(7) == 13, "The 8th value in a sum series starting with 0 and 1 should be 13"

    print("tests passed")
