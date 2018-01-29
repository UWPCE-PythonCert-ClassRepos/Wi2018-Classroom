#!/usr/bin/env python3
# Series 1
a_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(a_list)
response = 'Kiwi' #input('Please enter another fruit: ')
a_list.append(response)
print(a_list)
response = '4' #input('Please enter a number: ')
print(response + ' ' + a_list[(int(response) - 1)])
a_list = ['Cherries'] + a_list
a_list.insert(0, 'Bananas')
for fruit in a_list:
    if 'P' in fruit:
        print(fruit, end=' ')
# Series 2
print(a_list)
del a_list[-1]
print(a_list)
response = 'Pears'#input('Please enter a fruit to remove: ')
try:
    del a_list[a_list.index(response)]
except:
    print('Fruit not found.')

# TODO: Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.

# Series 3
for fruit in a_list:
    rep = input('Do you like '+ fruit.lower() +'? ')
    while (rep.lower() != 'yes') and (rep.lower() != 'no'):
        rep = input('Please respond with \'yes\' or \'no\': ')
    if rep.lower() == 'no':
        del a_list[a_list.index(fruit)]
print(a_list)

# Series 4
"""Make a copy of the list and reverse the letters in each fruit in the copy.
Delete the last item of the original list. Display the original list and the copy."""
