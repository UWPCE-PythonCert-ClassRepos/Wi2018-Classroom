'''FizzBuzz: print a list of 1 to 100. For numbers that are a multiple of 3 print fizz. For numbers that are a multiple of 5 print buzz. For numbers that are a multiple of 3 AND 5 print FizzBuzz. 
'''
#Create the list of number 1 to 100

a_list=list(range(1,101))

#Loop through the list of numbers to using modulo functionevaluate the remainders  . Print results. 
for i in a_list: 
  if i%3==0 and i%5==0:
    print('FizzBuzz')
  if i%3==0:  
    print('Fizz')
  elif i%5==0:
    print('Buzz')
  else:
    print(i)