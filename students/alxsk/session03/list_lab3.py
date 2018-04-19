'''Series 3 of list lab exercises'''
#Create a list that contains Apples, Pears, Oranges, and Peaches. 4 fruits. Print the list.
fruity=["Apples", "Pears", "Oranges", "Peaches"]

#Lowercase the items in the string
[f.lower() for f in fruity]

#Ask the user if the like each fruit
print("Do you like ",end='')

question=input("? ")


'''
Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
For each “no”, delete that fruit from the list.
For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
Display the list.
'''