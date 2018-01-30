'''A Fibonaccie series function. The function returns the nth number in the series.'''
def fibonacci(n):
    if n<=1: 
    	return n
    else: 
    	return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(8))