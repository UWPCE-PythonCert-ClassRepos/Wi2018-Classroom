def fizz_buzz(n1 = 1, n2 = 100):
    remainder = 0
    num_list = []
    num_list.extend(range(n1, n2+1))
    #print(num_list)
    for num in num_list:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizz_buzz()
