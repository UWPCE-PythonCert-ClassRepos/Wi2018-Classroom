
def fibonacci(n):
    #if n == 0:
    if n == 0 or n == 1:
        return 0
    #elif n == 1:
    elif n == 2:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)

print(fibonacci(10))


def lucas(n):
    if n == 0:
        return 0
    elif n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n-2)+lucas(n-1)

print(lucas(10))

