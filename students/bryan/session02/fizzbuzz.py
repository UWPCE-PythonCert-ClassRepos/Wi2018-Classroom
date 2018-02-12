def fizzbuzz():
    """print numbers from 1 to 100 inclusive. 
        for multiples of 3 print fizz instead of numbers
        for multiples of 5 print buzz instead of numbers
        for multiples of both print fizzbuzz """
    print("hi")
    idx = 1
    while idx <= 100:
        if idx % 3 == 0 and idx % 5 == 0:
            print('fizzbuzz')
        elif idx % 3 == 0:
            print ('fizz')
        elif idx % 5 == 0:
            print ('buzz')
        else:
            print (idx)
        idx += 1
        
def fizzbuzz2():
    """try doing fizzbuzz a different way. Using list comprehension"""
    print("hi")
    mylist = list(range(1,101))
    mylist[:] = ["fizzbuzz" if x % 3 == 0 and x % 5 == 0 
        else "fizz" if x % 3 == 0 
        else "buzz" if x % 5 == 0 
        else x for x in mylist]
    print(mylist)

#fizzbuzz()
fizzbuzz2()



