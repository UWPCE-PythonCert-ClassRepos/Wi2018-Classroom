#!/usr/bin/env python3

#Series 1

"""Create a list that contains “Apples”, “Pears”, “Oranges” 
and “Peaches”."""
fruits = ['Apples','Pears','Oranges','Peaches']

#Display the list
print(fruits)

#Ask the user for another fruit and add it to the end of the list.
user_fruit = input("add a fruit of your choice > ")
fruits.append(user_fruit)

#Display the list
print(fruits)

"""Ask the user for a number and display the number 
back to the user and the fruit corresponding to that number 
(on a 1-is-first basis). """
user_number = input("enter a number from 1 to 5 > ")
print (user_number," ",fruits[int(user_number)-1])

"""Add another fruit to the beginning of the list using “+” 
and display the list."""
fruits = ["Mangoes"]+fruits
print(fruits)

"""Add another fruit to the beginning of the list using 
insert() and display the list."""
fruits.insert(0,'Grapes')
print(fruits)

#Display all the fruits that begin with “P”, using a for loop.
for i in range(len(fruits)):
    chosen_fruit=fruits[i]
    if chosen_fruit[0]=="P":
        print(chosen_fruit)

#Series 2

#Display the list.
print(fruits)

#Remove the last fruit from the list.
fruits=fruits[:-1]

#Display the list.
print(fruits)

#Ask the user for a fruit to delete, find it and delete it.
user_removed_fruit = input("enter a fruit to remove > ")
fruits_to_remove=[]
for i in range(len(fruits)):
    if fruits[i]==user_removed_fruit:
        fruits_to_remove.append(fruits[i])
new_list=[x for x in fruits if x not in fruits_to_remove]
print(new_list)

'''(Bonus: Multiply the list times two. Keep asking 
until a match is found. Once found, delete all occurrences.)'''

new_list=new_list*2
fruits_to_remove=[]
while fruits_to_remove==[]:
    user_removed_fruit = input("enter a fruit to remove > ")
    for i in range(len(new_list)):
        if new_list[i]==user_removed_fruit:
            fruits_to_remove.append(new_list[i])
newer_list=[x for x in new_list if x not in fruits_to_remove]
print(newer_list)

#Series 3

"""Ask the user for input displaying a line like 
“Do you like apples?” for each fruit in the list 
(making the fruit all lowercase).
For each “no”, delete that fruit from the list.
For any answer that is not “yes” or “no”, prompt the user to 
answer with one of those two values (a while loop is good here)
Display the list."""

print(fruits)
fruits_to_remove=[]
for i in range(len(fruits)):
    question = "Do you like " + fruits[i].lower() + "? (yes/no) > "
    user_response=input(question)
    while user_response not in ['yes','no']:
        user_response=input("Please respond only with a 'yes' or 'no'")
    if user_response=='no':
        fruits_to_remove.append(fruits[i])
user_preferred_fruits=[x for x in fruits if x not in fruits_to_remove]
print(user_preferred_fruits)

#Series 4

'''Once more, using the list from series 1: Make a copy of 
the list and reverse the letters in each fruit in the copy.'''
fruits_copy=fruits[:]
for i in range(len(fruits_copy)):
    reversed=''
    for j in range(len(fruits_copy[i])):
        reversed+=fruits_copy[i][-1-j]
    fruits_copy.append(reversed)
fruits_copy = [x for x in fruits_copy if x not in fruits]


'''Delete the last item of the original list. 
Display the original list and the copy.'''
fruits.remove(fruits[len(fruits)-1])
print(fruits)
print(fruits_copy)


