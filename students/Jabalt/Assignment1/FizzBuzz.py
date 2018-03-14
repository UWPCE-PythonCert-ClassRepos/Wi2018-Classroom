for n in range (100):
    if n % 3 == 0 and n % 5 == 0:
        print ("fizzbuzz")
        continue
    if n % 3 == 0:
         print("fizz")
         continue
    if n % 5 ==0 :
         print("buzz")
         continue
    else:
         print (n)
        

