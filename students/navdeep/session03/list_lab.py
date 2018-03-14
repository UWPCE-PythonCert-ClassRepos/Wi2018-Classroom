def printFruits(fruit_list, index = None):
    """
    Prints the sequence of fruits
    :param fruit_list: the list of containing different fruits
    :param index: if a fruit in a specific index needs to be accessed
    """
    if index == None:
        print(fruit_list)
    else:
        print("Here is the fruit you chose to see: " + fruit_list[index])

def userAddToList(fruit_list):
    """
    Allows user to add to the fruit list
    :param fruit_list: the list of fruits
    """
    new_fruit = input("Enter a new fruit: ")
    fruits.append(new_fruit)

def askUserDisplay(fruit_list):
    """
    Asks the user which fruit they want to see based on the one-off index they select
    :param fruit_list: the list of fruits
    """
    index = int(input("Select a number between 1 and {} to "
                  "display fruit: ".format(len(fruit_list))))
    while index < 1 or index > len(fruit_list):
        index = int(input("Select a number between 1 and {} to "
                      "display fruit: ".format(len(fruit_list))))
    printFruits(fruit_list, index-1)

def addMoreFruits(fruit_list):
    """
    Adds fruits to the list using two different methods (+ and .insert())
    :param fruit_list: the list of fruits
    :return: and new list of fruits that contain new fruits in the beginning of the list
    """
    new_fruit = ["Bananas"]
    new_fruit += fruit_list
    new_fruit.insert(0, "Grapefruit")
    return new_fruit

def displayPFruits(fruit_list):
    """
    Displays the fruits in the list that begin with the letter 'P'
    :param fruit_list: the list of fruits
    """
    p_list = []
    for fruit in fruit_list:
        if fruit[0].upper() == "P":
            p_list.append(fruit)
    print("Fruits that begin with P: ", p_list)

def RemoveLastFruit(fruit_list, fruit = None):
    """
    Removes either a specific fruit (including repeats) from the list or the last fruit in the list
    :param fruit_list: the list of fruits
    :param fruit: If provided, the specific fruit to be removed from the list
    """
    if fruit == None:
        del fruit_list[len(fruit_list) - 1]
    else:
        for item in fruit_list:
            if item.lower() == fruit.lower():
                fruit_list.remove(item)

def UserDelete(fruit_list):
    delete_fruit = input("Enter a fruit to delete: ")
    RemoveLastFruit(fruit_list, delete_fruit)

def UserPreference(fruit_list):
    """
    Determines what fruits the user likes and does not like.  For the fruits the user
    does not like, those fruits will be removed from the original fruit list
    :param fruit_list: the list of fruits
    """
    preference = ""
    freeze_list = []
    for fruit in fruit_list:
        freeze_list.append(fruit)
    for i in freeze_list:
        preference = input("Do you like {}? ".format(i.lower()))
        while preference.lower() != "no" and preference.lower() != "yes":
            preference = input("Do you like {}? ".format(i.lower()))
        if preference.lower() == "no":
            RemoveLastFruit(fruit_list, i)

def copyReverse(fruit_list):
    """
    Creates a copy of the fruit list.  For each fruit in the copy list, the fruit will be spelled backwards
    :param fruit_list: the list of fruits
    :return: the copy of the new fruit list with each fruit spelled backwards
    """
    copy_fruits = []
    reverse_fruit = ""
    for fruit in fruit_list:
        reverse_fruit = fruit[-1::-1]
        copy_fruits.append(reverse_fruit)
    return copy_fruits

print("SERIES 1:")
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
printFruits(fruits)
userAddToList(fruits)
printFruits(fruits)
askUserDisplay(fruits)
print()
fruits = addMoreFruits(fruits)
printFruits(fruits)
print()
displayPFruits(fruits)
print()

print("SERIES 2:")
printFruits(fruits)
RemoveLastFruit(fruits)
printFruits(fruits)
UserDelete(fruits)
printFruits(fruits)

print("SERIES 3:")
UserPreference(fruits)
printFruits(fruits)

print("SERIES 4:")
reverse_list = copyReverse(fruits)
RemoveLastFruit(fruits)
printFruits(reverse_list)
printFruits(fruits)