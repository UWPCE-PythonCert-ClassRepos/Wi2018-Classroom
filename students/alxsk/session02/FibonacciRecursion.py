<<<<<<< HEAD
'''A Fibonaccie series function. The function returns the nth number in the series.'''
def fibonacci(n):
    if n<=1: 
    	return n
    else: 
    	return fibonacci(n-1)+fibonacci(n-2)
=======
'''A Fibonaccie series function. The function returns the nth number in the series.'''
def fibonacci(n):
    if n<=1: 
    	return n
    else: 
    	return fibonacci(n-1)+fibonacci(n-2)
>>>>>>> 9dfb3ae8d0d8ed5650207ce3e06d3045cfeefe24
print(fibonacci(8))