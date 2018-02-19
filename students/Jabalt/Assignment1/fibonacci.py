def fibonacci(n):
    if n == 1:
#the first fibonacci nubmer is 1 
        return 1
    elif n ==2 :
        return 1
    elif n >2 :
        return fibonacci(n-1) + fibonacci(n-2)
for n in range (1,11):
     print (fibonacci(n))
        
