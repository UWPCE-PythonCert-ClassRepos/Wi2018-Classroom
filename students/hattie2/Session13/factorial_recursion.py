def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))

for x in range(4):
    print(factorial(x))
    