
#Name:Manuel Duarte
#program:FizzBuzz
#Program prints Buzz if the number is divisible by 3
#or if number is divisible by 5 and if it is divisible by both 3 and 5
# print fuzzbuzz


for fizzbuzz in range(100):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0: #divisible by either 3 or 5
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0: #if divisible by 3 statement
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0: #if divisible by 5
        print("buzz") #prints buzz
        continue
    print(fizzbuzz) #prints Fizzbuzz
