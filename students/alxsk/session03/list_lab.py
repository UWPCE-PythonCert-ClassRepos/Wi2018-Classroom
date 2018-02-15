'''Series 1 of list lab exercises'''
#Create a list that contains Apples, Pears, Oranges, and Peaches. 4 fruits. Print the list.
fruity=["Apples", "Pears", "Oranges", "Peaches"]
print("Fruity smoothie contains...")
print(fruity)
print()

#External input in cmd prompt for another fruit. Append the input to the list. Print list.
add=input("Add a fruit: ")
fruity.append(add)
print(fruity)
print()

# Now there's a list of 5 fruits. Return the fruit based on the number input from cmd prompt 1 to n. 
# Pad the list make the fruit items have a non-zero index.
fruity.insert(0,'0index_pad')
print("Identify a fruit in the smoothie. Pick a number 1 to "+ str(len(fruity)-1),end='')
pick_number=input(": ")

#change the class of input to a integer. 
int_number=int(pick_number)
print(fruity[int_number])
print()

#Insert 2 fruits fruit to the front of the list.
print("Now adding jackfruit to the smoothie...")
#using insert command. Not running fruity=["Pineapples"]+fruity because of 0index_pad.
fruity.insert(1,"jackfruit")
print("Ingredients in smoothie are ",end='')
print(fruity[1:])
print()

#Loop through each item in the list. Print the items that begin with P.
print("Which fruits begin with 'P'?")
for fruit in fruity:
	if fruit[0]=="P":
		print(fruit)

