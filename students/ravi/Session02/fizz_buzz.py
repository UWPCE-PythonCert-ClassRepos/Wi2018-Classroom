for i in range(100):
    if (i+1)%3+(i+1)%5==0:
        print('FizzBuzz')
    else:
        if (i+1)%3==0:
            print('Fizz')
        else:
            if (i+1)%5==0:
                print('Buzz')
            else:
                print(i+1)