#!/usr/bin/env python3


#Part 1
fruit = ["Apples", "Pears", "Oranges", "Peaches"]

print(fruit)

response = input("add a fruit to the list...")
fruit.append(response)

print(fruit)

user_number = input("write the number of the fruit you want  ")

print(user_number)
print(fruit[int(user_number) - 1])

fruit = ["Bananas"] + fruit
print(fruit)

fruit.insert(0, "Grapes")	
print(fruit)

for x in fruit:
	if x[0] == "P":
		print(x)

##Part 2
# print(fruit)
# fruit.pop()
# print(fruit)

# deletefruit = input("which fruit should be removed?")

# #Bonus
# while deletefruit not in fruit:
# 	fruit += fruit
# 	print(fruit)
# 	deletefruit = input("which fruit should be removed?")

# while deletefruit in fruit:
# 	fruit.remove(deletefruit)
# print(fruit)

##Part3
# lowerFruit = [x.lower() for x in fruit]

# appleResponse = ""
# listCounter = 0

# while listCounter < len(lowerFruit):
# 	appleResponse = input("Do you like " + lowerFruit[listCounter] + "?")

# 	while appleResponse not in ("yes","no"):
# 		print("you must respond with 'yes' or 'no'")
# 		appleResponse = input("Do you like " + lowerFruit[listCounter] + "?")

# 	if appleResponse == "no":
# 		lowerFruit.remove(lowerFruit[listCounter])
# 		print(lowerFruit)
# 	else:
# 		print(lowerFruit)
# 		listCounter += 1

#Part 4
copyList = []

for f in fruit:
	copyList.append(f[-1:] + f[1:-1] + f[:1])

print(copyList)
fruit.pop()
print(fruit)






