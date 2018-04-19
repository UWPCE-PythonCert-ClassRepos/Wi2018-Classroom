def fizzBuzz(max=100):

    # entering while loop---check that max is > 1
    if max < 1:
        raise ValueError("Make sure that 'max' is a positive nonzero value")

    valuesList = []
    
    i = 1

    while i <= max:
        value = ''

        if i%3 == 0:
            value += 'Fizz'

        if i%5 == 0:
            value += 'Buzz'

        if value == '':
            value = i

        valuesList.append(value)

        i += 1

    return valuesList


# try it out
list = fizzBuzz(100)

for ind, value in enumerate(list):
    print(ind+1,value)
