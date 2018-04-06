 #!/usr/bin/env python3

 """
Series 1
    Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
    Display the list (plain old print() is fine…).
    Ask the user for another fruit and add it to the end of the list.
    Display the list.
    Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
    Add another fruit to the beginning of the list using “+” and display the list.
    Add another fruit to the beginning of the list using insert() and display the list.
    Display all the fruits that begin with “P”, using a for loop.
"""
fruits = ['Apples', 'Pears', 'Oranges','Peaches']
print (fruits)
new_fruits = input ('Enter another fruit that is not in the fruit list \n ')
fruits.append(new_fruits.lower())
print (fruits)

print ('The list has the following', len(fruits),'fruits',fruits)

number = int (input('Enter a number between 1 and 5 : \n'))
choice_fruit = fruits[int(number)-1]
if number <= 0:
	print('Please enter valid number between 1 and 5 ')
if number > len(fruits):
	print ('the number you entered is out of the range')
else :
	print ('you entered' ,number,'and the fruit is', choice_fruit)





#[Mango, Pineapple,Papay,Lemon,Banana]
fruits = ['Lemon'] + fruits
print (fruits)
fruits.insert(0,'Mango')
print(fruits)

#fruit_p =[]
for i in fruits:
	if i[0] == 'p':
		print('all the fruit with lette p are ' ,(i) )#('All the fruits that begin with letter P are'(i))

	

'''


"""
Series 2
Using the list created in series 1 above:
    Display the list.
    Remove the last fruit from the list.
    Display the list.
    Ask the user for a fruit to delete, find it and delete it.
    (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
"""

'''
print (fruits)
fruits.remove(fruits[len(fruits)-1])

print(fruits)
newf = input ('plsease enter fruit to delete \n' .lower())

for item in fruits:
	if item == newf.lower():
		fruits.remove(item)
	elif item != newf:
		print('please enter fruit from the list')
	else:
		print (fruits)

"""
Series 3
    Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
    For each “no”, delete that fruit from the list.
    For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
    Display the list.
"""


for item in fruits[:]:
	request = input ('Do you like {} ? \n'.format(item.lower()))
	while request.lower()not in ('yes','no'):
		print ('please enter yes or no')
		request = input ('Do you like  {} ? \n'.format(item.lower()))
	if request == "no":
		fruits.remove(item)
print (fruits)
		

"""

Series 4
Make a copy of the list and reverse the letter in each fruits
Delete the last item of the original list.

"""
print(fruits)
fruit2 = []
for item in fruits:
	fruit2.append(item[::-1])

print (fruit2)
del fruits[len(fruits)-1]
print (fruits)
new_fruits = fruits[:]