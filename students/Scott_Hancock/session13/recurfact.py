def recurfact(n):
    if n == 1:
        return 1
    return n * recurfact(n - 1)
