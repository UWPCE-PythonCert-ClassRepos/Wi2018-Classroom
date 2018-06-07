#!/usr/bin/env python

# Programming in Python B Spring 2018
# April 22, 2018
# Lession 03 - saved in Session13 -
# Factorial
# Tracy Allen - git repo https://github.com/tenoverpar/Wi2018-Classroom


def factorial(val):
    """
    Recursive Function: mathematical factorial (!number)
    :return: int, factorial
    """
    if val == 0:
        return 1
    else:
        return val * factorial(val - 1)


# Test the the factorial with assert statement
assert factorial(6) == 720
assert factorial(2) == 2
assert factorial(5) == 120


# Testing overkill now.
def test_factorial():
    fiblist = [1, 2, 6, 24, 120, 720]
    nlist = []
    print("Running factorial test 1-6")
    print("*********************")
    for i in range(1, 7):
        nlist.append(factorial(i))
        print(list(nlist))
    assert fiblist == nlist


def main():
    test_factorial()


if __name__ == "__main__":
    main()
