def fizz_buzz():
    for num in range(101):
        if num % 3 == 0 and num % 5 == 0:
            print(num)
            print("Fizz_Buzz")
        elif num % 3 == 0:
            print(num)
            print ("Fizz")
        elif num % 5 == 0:
            print (num)
            print ("Buzz")
