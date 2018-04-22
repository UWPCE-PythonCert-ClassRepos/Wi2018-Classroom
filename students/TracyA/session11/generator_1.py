#!/usr/bin/env python

"""
Write a few generators
1. sum of integers
2. doubler
3. Fibonacci sequence
4. Prime numbers
"""


def intsum(i=0):
    """
    sum of integers
    """
# For use with test_generator.py
    n = 0
    while True:
        i += n
        yield i
        n += 1
# For use with __main__  test printing

# def intsum(x):
#     """
#     sum of integers
#     """
    # n = 0
    # for i in range(x):
    #     n = n + i
    #     yield n


# For use with __main__  test printing
# def doubler(x, y):
#     """
#     Doubler, Each value is double the previous value
#     """
#     for i in range(x, y):
#         yield 2 ** (i-1)

# For use with test_generator.py
def doubler(i=1):
    yield i
    while True:
        i *= 2
        yield i


# For use with __main__  test printing
# def fib(n):
#     """
#     Fibonacci sequence up to a max value
#     f(n) = f(n-1) + f(n-2)
#     """
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b

# For use with test_generator.py
def fib():
    a, b = 0, 1
    while True:
        yield a
        b = a + b
        yield b
        a = a + b

# For use with __main__  test printing
# def prime(max):
#     """
#     Check for prime numbers
#     """
#
#     primes = []
#     for n in range(2, max):
#         n_prime = True
#         for p in primes:
#             if n % p == 0:
#                 n_prime = False
#                 break
#         if n_prime:
#             primes.append(n)
#             yield n


def prime():
    """
    Check for prime numbers
   """
    b = 1
    yield 2
    while True:
        b += 2
        for a in range(2, b):
            if b % a == 0:
                break
        else:
            yield b

# if __name__ == "__main__":
#
#     print("1. Sum of integers:")
#     print(list(intsum(20)))
#
#     print("2. Double the previous value:")
#     print(list(doubler(1, 20)))
#
#     print("3. Fibonaci sequence:")
#     print(list(fib(20)))
#
#     print("4. Prime numbers less than 20:")
#     for p in prime(20):
#         print(p)
