
"""
    Create a new module series.py in the session02 folder in your student folder.
        In it, add a function called fibonacci.
        The function should have one parameter n.
        The function should return the nth value in the fibonacci series.
    Ensure that your function has a well-formed docstring

    series is like: 0, 1, 1, 2, 3, 5, 8, 13, ...
"""

def fibonacci(n):
    """Prints the nth value of the Fibonacci sequence"""
    series = [0, 1]
    while len(series)<n:
        series.append(sum(series[-2:]))
    return series[n-1]

print(fibonacci(4))

# Should be like: 2, 1, 3, 4, 7, 11, 18, 29, ...
def lucas(n):
    """Prints the nth value of the Lucas Numbers sequence"""
    series = [2, 1]
    while len(series)<n:
        series.append(sum(series[-2:]))
    return series[n-1]

print(lucas(5))


def sum_series(n, a=0, b=1):
    """3 params: n is number in the sum series, and a and b are the first two in the series"""
    series = [a, b]
    while len(series)<n:
        series.append(sum(series[-2:]))
    return series[n-1]

assert sum_series(4) == fibonacci(4)
assert sum_series(4, 2, 1) == lucas(4)