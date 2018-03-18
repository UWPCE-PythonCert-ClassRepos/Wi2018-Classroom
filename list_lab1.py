
# python list_lab.py
List_fruits = ["Apples", "Pears", "Oranges", " Peaches "]

print(List_fruits)

new = input("Please write your favorate fruit:")

List_fruits.append(new)

print(List_fruits)

ind = int(input("give me an index: "))

print("you selected fruit number: {}, which is {}".format(ind, List_fruits[ind - 1]))
print()
print("All the fruit:\n", List_fruits)
print()

List_fruits.insert(0, 'Mango')

print("Added a Mango at the beginning:\n", List_fruits)

print()
print("All the P List_fruits:")
for fruit in List_fruits:
    if fruit[0].lower() == 'p':
        print(fruit)
print()

d_List_fruits = List_fruits * 2

print("All the List_fruits are:", List_fruits)
ans = input("Which fruit would you like to delete? >")
while ans in d_List_fruits:
    d_List_fruits.remove(ans)

print("\nWith fruit deleted:\n", d_List_fruits)
d_List_fruits = List_fruits * 2
d_List_fruits_new = []
for fruit in d_List_fruits * 2:
    if fruit != ans:
        d_List_fruits_new.append(fruit)

print("\nWith fruit deleted another way:\n", d_List_fruits_new)
print()

# Series 3

d_List_fruits = List_fruits[:]

for fruit in List_fruits[:]:  # loop through a copy!
    ans = input("Do you like: %s? " % fruit)
    if ans[0].lower() == 'n':  
        while fruit in List_fruits:  
            List_fruits.remove(fruit)
    elif ans[0].lower() == 'y':
        pass
    else:
        print("Please answer yes or no:")


print("\nLists of the fruits you like")
print(List_fruits)
print()

# Series 4

r_fruits = []
for fruit in List_fruits:
    r_fruits.append(fruit[::-1])
print("Reversed list of the fruits")
print(r_fruits)




