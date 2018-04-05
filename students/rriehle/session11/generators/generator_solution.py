#!/usr/bin/env python3


def intsum():
    ''' The for loop herein perhaps makes this eary to grok. '''
    total = 0
    for i in range(20):
        total += i
        yield total


def intsum2():
    ''' The infinite loop herein is more inline with the raison d'être of a generator. '''
    total = i = 0
    while True:
        total += i
        yield total
        i += 1


def doubler():
    total = 1
    while True:
        yield total
        total *= 2


def fib():
    my_last = 0
    my_next = 1
    yield my_next
    while True:
        my_current = my_last + my_next
        yield my_current
        my_last = my_next
        my_next = my_current


def fib2():
    ''' Is this better or does it obfuscate? '''
    my_last, my_next = 0, 1
    while True:
        yield my_next
        my_last, my_next = my_next, my_last + my_next


def prime0():
    ''' Working out the basic brute-force logic. This might get ugly. '''
    my_range = 9999999
    for i in range(1, my_range):
        for j in range(2, my_range):
            if i == j:
                yield i
            elif i % j == 0:
                break


def prime1():
    ''' A little better '''
    j = 1
    while True:
        j += 1
        # Need to jack the range to 1 past candidate j otherwise the yeild condition never hits
        # That feels kludgey
        for i in range(2, j + 1):
            if i == j:
                yield j
            elif j % i == 0:
                break


def prime():
    ''' Perhaps best '''
    j = 1
    while True:
        j += 1
        for i in range(2, j):
            # If we find a divisor that produces no reminder then j is not prime
            if j % i == 0:
                break
        else:
            # If we get all the way to the top of the range without breaking then we have a prime
            # Note that the else is on the for loop and not on the if statement!
            yield j


if __name__ == '__main__':
    my_test = prime()
    for _ in range(22):
        print(next(my_test))
