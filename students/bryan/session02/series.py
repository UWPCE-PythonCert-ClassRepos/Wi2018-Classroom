def fibonacci(n=0):
    """Fibonacci series. Takes one arguement n. Returns the nth value in the fibonacci series"""
    #fib(n) = fib(n-2) + fib(n-1)
    print("hello")

    if n == 0:
        return(0)
        
    elif n == 1:
        return(1)
    elif n == 2:
        return(1)
    else:
        #start at n = 3
        fibn2 = 1 # initialize n - 2
        fibn1 = 1 # initialize n - 1
        for i in range(2, n):
            value = fibn2 + fibn1 #recursive def of fibonacci series
            fibn2 = fibn1 #move it back a notch
            fibn1 = value # move it back a notch
        return(value)

x = fibonacci(6)
print(x)

