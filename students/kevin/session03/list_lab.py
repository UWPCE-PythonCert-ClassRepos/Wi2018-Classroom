#!/usr/bin/env python

# Series 1
print('\nSeries 1\n')
my_list = ['Apples', 'Pears', 'Oranges', 'Peaches']

# Display the list
print(my_list,'\n')

# Prompt user for fruit to add to list
response = input("Please enter another fruit to add to the list: ")

my_list.append(response)

# Display the list again
print(my_list,'\n')

while not response.isdigit():
    response = input(
        "Give me a number and I'll return that fruit in the list (or <Enter> to skip): ")
    if not response:
        break

try:
    print(my_list[int(response) - 1])
except:
    # Cannot print if user broke out of above loop or if the index
    # is out of range
    print("Whoops, can't find that fruit!")
    pass

my_list = ['Cherry'] + my_list
print(my_list)
my_list.insert(0, 'Kiwi')
print(my_list)

# print all fruits starting with 'p'
for fruit in my_list:
    if fruit[0].lower() == 'p':
        print(fruit)

        
# Series 2
print('\n\nSeries 2:\n')

print(my_list)

my_list.pop(-1)

print(my_list, '\n')

while not response in my_list:
    response = input(
        "Name a fruit in the list to delete (or <Enter> to skip): ")
    if not response:
        response = ''
        break
    if response not in my_list:
        print("The fruit you provided is not in the list. The list has grown. Please try again.\n")
        my_list *= 2
        print(my_list)


while response in my_list:
    my_list.remove(response)

print(my_list, '\n')


# Series 3
print('\nSeries 3:\n')
for fruit in set(my_list[:]):
    response = ''
    while response not in ['yes', 'no']:
        response = input("Do you like {}? [yes|no]: ".format(fruit.lower()))

    if response == 'no':
        while fruit in my_list:
            my_list.remove(fruit)

print('\n{}\n'.format(my_list))


# Series 4
print('\nSeries 4:\n')

my_list_cp = my_list[:]

for count in range(len(my_list_cp)):
    my_list_cp[count] = my_list_cp[count][::-1]

my_list.pop()

print(my_list, my_list_cp)
