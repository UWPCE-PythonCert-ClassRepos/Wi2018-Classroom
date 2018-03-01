<<<<<<< HEAD
'''FizzBuzz: print a list of 1 to 100. For numbers that are a multiple of 3 print fizz. For numbers that are a multiple of 5 print buzz. For numbers that are a multiple of 3 AND 5 print FizzBuzz. 
'''
#Create the list of number 1 to 100

a_list=list(range(1,101))

#Loop through the list of numbers using modulo in a series of if/else functions to evaluate each number. Print results. 
for i in a_list: 
  if i%3==0 and i%5==0:
    print('FizzBuzz')
  if i%3==0:  
    print('Fizz')
  elif i%5==0:
    print('Buzz')
  else:
    print(i)
=======
'''FizzBuzz: print a list of 1 to 100. For numbers that are a multiple of 3 print fizz. For numbers that are a multiple of 5 print buzz. For numbers that are a multiple of 3 AND 5 print FizzBuzz. 
'''
#Create the list of number 1 to 100

a_list=list(range(1,101))

#Loop through the list of numbers using modulo in a series of if/else functions to evaluate each number. Print results. 
for i in a_list: 
  if i%3==0 and i%5==0:
    print('FizzBuzz')
  if i%3==0:  
    print('Fizz')
  elif i%5==0:
    print('Buzz')
  else:
    print(i)
>>>>>>> 9dfb3ae8d0d8ed5650207ce3e06d3045cfeefe24
