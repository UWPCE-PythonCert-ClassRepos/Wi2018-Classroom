

def fibonacci(n):
    """The Fibonacci Series is a numeric series starting with the integers 0 and 1.
In this series, the next integer is determined by summing the previous two.
This function finds the nth value of the series
"""
    oneback = 1
    twoback = 0

    for i in range(n+1):
        if i == 0:
            current = 0
        elif i == 1:
            current = 1
        else:
            current = oneback + twoback
            twoback = oneback
            oneback = current
            #print(current)
    return current

def lucas(n):
    """The Lucas Numbers is a numeric series starting with the integers 2 and 1.
In this series, the next integer is determined by summing the previous two.
This function finds the nth value of the series
"""
    oneback = 1
    twoback = 2

    for i in range(n+1):
        if i == 0:
            current = twoback
        elif i == 1:
            current = oneback
        else:
            current = oneback + twoback
            twoback = oneback
            oneback = current
            #print(current)
    return current

def sum_series(n,oneback=1,twoback=0):
    """The sum_series creates a numeric series starting with the integers 0 and 1, or these numbers can be given.
In this series, the next integer is determined by summing the previous two.
This function finds the nth value of the series
"""
    for i in range(n + 1):
        if i == 0:
            current = twoback
        elif i == 1:
            current = oneback
        else:
            current = oneback + twoback
            twoback = oneback
            oneback = current
            # print(current)
    return current

assert (sum_series(3)==2)
assert (sum_series(4)==3)