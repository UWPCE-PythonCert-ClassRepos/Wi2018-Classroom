
def fibonacci(n):
    #if n == 0:
    if n == 0 or n == 1:
        return 0
    #elif n == 1:
    elif n == 2:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)


######################################################################


def lucas(n):
    if n == 0:
        return 0
    elif n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n-2)+lucas(n-1)


#####################################################################


def sum_series(n, a=0, b=1):
    """produce nth number in fibonacci sereis with default a, b arguments 
         and nth number in lucas series if a, b arguments are set to 2 and 1"""
    if n == 0:
        return 0
    if n == 1:
        return a
    if n == 2:
        return b
    else:
        return sum_series(n-2,a,b)+sum_series(n-1,a,b)


#####################################################################


#testing output of fibonacci function
assert fibonacci(5) == 3
assert fibonacci(8) == 13

#testing output of lucas function
assert lucas(5) == 7
assert lucas(8) == 29

#testing output of sum_series with default a,b arguments
assert sum_series(5) == 3
assert sum_series(8) == 13

#testing output of sum_series function with values 2,1 assigned to a,b arguments
assert sum_series(5,2,1) == 7
assert sum_series(8,2,1) == 29

