
"""
recursive factorial
"""

# Oh shoot, it was supposed to be factorials! My bad.

def facto(n):
    if n == 1:
        return 1
    return n * facto(n-1)

print(facto(1), facto(2), facto(3), facto(4), facto(5))
print(5*4*3*2)

"""
Write a recursive fibonacci sequence
"""


# def fibo(n):
#     if n == 1:
#         return 1
#     elif n == 0:
#         return 0
#     else:
#         return fibo(n-1) + fibo(n-2)

# print(fibo(0), fibo(1), fibo(2), fibo(3), fibo(4), fibo(5), fibo(6))





