#!/usr/bin/env python3

#Series 1
fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit)

response = input("Provide another fruit that is not currently in the fruit list: ")

fruit.append(response.capitalize())
print(fruit)


response2 = input("Choose a number between 1 and 5: ")
choice_num = response2
choice_fruit = fruit[int(response2)-1]

print(choice_num, choice_fruit)

fruit = ["Strawberries"] + fruit
print(fruit)
fruit.insert(0, "Pomegranate")
print(fruit)

for item in fruit:
    if item[0] == "P":
        print(item)


#Series 2
print(fruit)
fruit.remove(fruit[len(fruit)-1])
print(fruit)

response3 = input("Choose a fruit to remove from the list: ")
for item in fruit:
    if item == response3.capitalize():
        fruit.remove(item)
print(fruit)


#Series 3
for item in fruit[:]:
    response = input("Do you like {}?".format(item.lower()))
    while response.lower() not in ("yes", "no"):
        print("Please enter yes or no")
        response = input("Do you like {}?".format(item.lower()))
    if response == "no":
        fruit.remove(item)
print(fruit)


#Series 4
fruit2 = []
for item in fruit:
    fruit2.append(item[::-1])

print(fruit2)
del fruit[len(fruit)-1]
print(fruit)

