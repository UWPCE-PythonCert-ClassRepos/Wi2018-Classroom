def fibonacci(n):
    """
    Produces
    :param n:
    :return: 
    """

    fibList = [0, 1]

    while len(fibList) < n:
        fibList.append(fibList[-2] + fibList[-1])

    return fibList[n-1]


def lucas(n):
    """
    Docstring goes here
    """

    lucList = [2, 1]

    while len(lucList) < n:
        lucList.append(lucList[-2] + lucList[-1])

    return lucList[n-1]


def sumSeries(n, a=0, b=1):
    """
    Docstring goes here
    """

    sumList = [a, b]

    while len(sumList) < n:
        sumList.append(sumList[-2] + sumList[-1])

    return sumList[n-1]


assert (fibonacci(8) == 13),"The 8th value in the Fibonacci sequence should be 13"
assert (lucas(8) == 29),"The 13th value in the Fibonacci sequence should be 29"
assert (sumSeries(8) == 13),"The 8th value in a sum series starting with 0 and 1 should be 13"
