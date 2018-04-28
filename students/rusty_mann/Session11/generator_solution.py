
def intsum(i=0):
    n=0
    while True:
        i += n
        yield i
        n += 1

def doubler(i=1):
    yield i
    while True:
        i *= 2
        yield i

def fib():
    a,b = 0,1
    while True:
        yield a
        b = a+b
        yield b
        a = a+b

def prime():
    b = 1
    yield 2
    while True:
        b += 2
        for a in range(2,b):
            if b % a == 0:
                break
        else:
            yield b
