count = 1
for i in range(100):
    if (count % 5 == 0) and (count % 3 == 0):
        print('FizzBuzz')
    elif count % 3 == 0:
        print('Fizz')
    elif count % 5 ==0:
        print('Buzz')
    else:
        print(count)
    count += 1