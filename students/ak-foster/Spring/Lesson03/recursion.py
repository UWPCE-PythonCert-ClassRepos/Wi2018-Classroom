#!/usr/bin/env python3

def Fib(i):
    seq = list(i for i in range(1, i + 1))

    def multiply(seq):
        if len(seq) > 1:
            return multiply(seq[:-1]) * seq[-1]
        else:
            return seq[0]
    return multiply(seq)

print(Fib(10))