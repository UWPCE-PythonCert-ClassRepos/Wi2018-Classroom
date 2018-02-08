def fibonacci(x):
	"""Returns the xth term of the fibonacci series"""
	fib1 = 0
	fib2 = 1
	answer = 0

	for i in range(x):
		answer, fib1, fib2 = fib1, fib2, fib1 + fib2
	return answer

# print(fibonacci(0))
# print(fibonacci(3))
# print(fibonacci(5))
# print(fibonacci(100))

def lucas(x):
	"""Returns the xth term of the lucas series"""
	luc1 = 2
	luc2 = 1
	answer = 0

	for i in range(x):
		answer, luc1, luc2 = luc1, luc2, luc1 + luc2
	return answer

# print(lucas(8))

def sum_series(n,x = 0, y = 1):
	""" Create a sum series of n terms  with the imput x and y variables as the first two numbers"""
	num = 0
	output_series = []

	for i in range(n):
		num, x, y = x, y, x + y
		output_series.append(num)
	return output_series

print(sum_series(10))
print(sum_series(10, 2, 1))