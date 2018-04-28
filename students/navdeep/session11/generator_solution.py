def intsum(start = 0):
    current_sum = 0
    while True:
        current_sum += start
        yield current_sum
        start += 1

def doubler(start = 1):
    current_double = start
    while True:
        yield current_double
        current_double = current_double * 2

def fib(a = 0, b = 1):
    while True:
        yield b
        a, b = b, a + b

def prime(start = 2):
    prime = True
    while True:
        for i in range(2, start):
            if start % i == 0:
                prime = False
        if prime:
            yield start
        start += 1
        prime = True



