def intsum():
    x, y = 0, 0
    while True:
        yield y
        x += 1
        y += x

def doubler():
    x = 1
    while True:
        yield x
        x += x

def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b

def prime():
    # hmmm...
