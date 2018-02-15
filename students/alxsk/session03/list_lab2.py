'''Series 2 of list lab exercises '''
#Create a list that contains Apples, Pears, Oranges, and Peaches. 4 fruits. Print the list.
print("A basket of fruit contains ", end='')
fruity=["Apples", "Pears", "Oranges", "Peaches"]
print(fruity)
print()

#Pop the last fruit from the list. Print the list.
print("Removing the last fruit from the list, the new list is", end='')
fruity.pop(-1)
print(fruity)
print()

#Remove fruit from list. Use cmd prompt intry for the input. Print the list.
remove=input("Type a fruit from the list to remove: ")
fruity.remove(remove)
print("The new list is", end='')
print(fruity)