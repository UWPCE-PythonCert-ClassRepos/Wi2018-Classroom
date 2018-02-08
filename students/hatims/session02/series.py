def fibonacci(n, arg1=0, arg2=1):
    """
    The Fibonacci function has one parameter n.  And returns the nth value in the Fibonacci series.
    """
    if n < 1:
        return 1
    current,next=arg1,arg2
    for num in range(n):
        current,next=next,current+next
    return current
	
	
def lucas(n, arg1=2, arg2=1):
    """
    The Lucas function returns the nth value in the Lucas numbers series.
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    current,next=arg1,arg2
    for num in range(n):
        current,next=next,current+next
    return current    
		
def sum_series(arg1, arg2=0, arg3=1):
    """the sum_series with one required parameter and two optional parameters. The required parameter will determine which element in the series to print. 
    The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced.
    """
    if arg2==0 and arg3==1:
        return fibonacci(arg1, arg2, arg3)
    elif arg2==2 and arg3==1:
        return lucas(arg1, arg2, arg3)
	
	
assert fibonacci(22) == 17711
assert fibonacci(22, 3, 1) == 50549

assert lucas(29) == 1149851
assert lucas(29, 3, 1) == 1467662

assert sum_series(22) == 17711
assert sum_series(29, 2, 1) == 1149851



		
