
#Series 1

my_list=["Apples", "Pears", "Oranges", "Peaches"]

print(my_list)

my_list.append(input('Enter another type of fruit \n'))

print(my_list)

list_size= len(my_list)
fruit_num = input("Pick a number 1 through %d \n" % list_size )

print(my_list[int(fruit_num)-1])

my_list =['Durian'] + my_list

print(my_list)

my_list.insert(0,"Jackfruit")

print(my_list)

for fruit in my_list:
    if fruit[0] == "P":
        print(fruit)

# Series 2

print("Series 2")
print(my_list)

my_list.pop()

print(my_list)

response = (input("Which one do you want to remove?"))

while not response in my_list:
    response = (input("Which one do you want to remove?"))

my_list.remove(response)

print(my_list)

#Series 3
my_list=["Apples", "Pears", "Oranges", "Peaches"]

print("Series 3")
for fruit in my_list:
    response = input("Do you like %s \n" % fruit.lower())
    while response != "Yes" and response != "No":
        response = input("Please enter Yes or No \n")
    if response == "Yes":
        print("Cool, me too. \n")
    elif response == "No":
        print ("Yeah, they're gross.\n")
        my_list.remove(fruit)

print(my_list)

#Series 4
print("Series 4")

my_list=["Apples", "Pears", "Oranges", "Peaches"]
copy_list =[]

for fruit in my_list:
    copy_list.append(fruit[::-1])

my_list.pop()

print (my_list)
print(copy_list)






