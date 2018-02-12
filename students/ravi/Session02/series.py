def fibonacci(n):
    first=0                 #first Fibonacci term
    second=1                #second Fibonacci term
    fibonaccilist=[first,second]
    for i in range(2,n):    #start from 3rd term since 1st 2 already printed
        sum=first+second    #sum of previous 2 numbers in the series
        fibonaccilist.append(sum)
        first=second        #updates the new previous number-1
        second=sum          #updates the new previous number
    return(fibonaccilist)

def lucas(n):
    first=2                 #first Lucas term
    second=1                #second Lucas term
    lucaslist=[first,second]
    for i in range(2,n):    #start from 3rd term since 1st 2 already printed
        sum=first+second    #sum of previous 2 numbers in the series
        lucaslist.append(sum)
        first=second        #updates the new previous number-1
        second=sum          #updates the new previous number
    return(lucaslist)

def sum_series(n,first=0,second=1):
    sum_serieslist=[first,second]
    for i in range(2,n):    #start from 3rd term since 1st 2 already printed
        sum=first+second    #sum of previous 2 numbers in the series
        sum_serieslist.append(sum)
        first=second        #updates the new previous number-1
        second=sum          #updates the new previous number
    return(sum_serieslist)

def fibonacci1(n):
    return sum_series(n)


def lucas1(n):
    return sum_series(n,2,1)

assert fibonacci(5)==[0,1,1,2,3]    #0,1, 0+1=1, 1+1=2, 1+2=3
assert lucas(5)==[2,1,3,4,7]        #2,1, 2+1=3, 1+3=4, 3+4=7
assert fibonacci(5)==sum_series(5)  #as described and expected
assert lucas(5)==sum_series(5,2,1)  #as described and expected
assert fibonacci(5)==fibonacci1(5)  
assert lucas(5)==lucas1(5)