# Recursive algorithm to compute factorial
# rriehle 2018


def factorial(n):
    if n:
        return n * factorial(n - 1)
    return 1


# def factorial(n):
#     return n * factorial(n - 1) if n else 1


def test_factorial():
    assert 1 == factorial(1)
    assert 2 == factorial(2)
    assert 6 == factorial(3)
    assert 24 == factorial(4)
    assert 120 == factorial(5)


if __name__ == '__main__':
    print(factorial(5))
