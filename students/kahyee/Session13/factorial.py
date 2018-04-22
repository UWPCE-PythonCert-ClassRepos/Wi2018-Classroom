def factorial(n):
    while n > 0:
        return n * factorial(n-1)
    return 1
    
    

print([factorial(i) for i in range(20)])