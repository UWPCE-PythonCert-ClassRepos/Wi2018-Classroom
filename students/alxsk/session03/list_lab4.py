'''Series 1 of list lab exercises'''
#Create a list that contains Apples, Pears, Oranges, and Peaches. 4 fruits. Print the list.
print("Write a list of fruit. Then reverse the letters of each fruit. Compare lists. ")
fruity=["Apples", "Pears", "Oranges", "Peaches"]
print(fruity)

#Make a copy of the list. 
fruity_copy=fruity[:]

#Reverse the letters in each fruit in the list copy. Print list.
def reverse(f):
	reversed_f = []
	for fruit in fruity_copy:
		reversed_f.append(fruit[::-1])
	return reversed_f

print(reverse(fruity_copy))