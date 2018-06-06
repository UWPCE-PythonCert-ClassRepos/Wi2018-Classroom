def factorial(x, y=1):
    """
    Computes 1 * 2 * 3 * ... * (x-2) * (x-1) * x and returns as y
    :param x: (theoretically) any integer
    :return: y (another integer)
    """

    if x == 1:
        return y
    else:
        y *= x
        x -= 1
        return factorial(x, y)


p = factorial(10)
print(p)