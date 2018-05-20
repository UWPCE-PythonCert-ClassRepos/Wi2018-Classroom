import math

def intsum():
    a = 0
    b = 0
    while True:
        a += b
        yield a
        b += 1


def doubler():
    a = 1
    while True:
        yield a
        a *= 2


def fib():
    a,b = 0,1
    while True:
        yield b
        a, b = b, a+b


def prime():
    yield 2 # get this outlier out of the way first
    a = 3
    while True:
        for i in range(2, math.ceil(math.sqrt(a))+1):
            if a % i == 0:
                break
        else:
            yield a
        a += 2 # skip all even numbers to save some time