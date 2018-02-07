
#https://canvas.uw.edu/courses/1177831/assignments/4057042?module_item_id=8109752
## List Lab Exercise Series 1

def get_arg(msg):

    """Generic function to get user input"""

    arg=input(f"{msg} ([Enter] to quit)>>")

    if len(arg)>0:
        return [True,arg]
    else:
        print("leaving...")
        return [False]

def ordinal(val):
    """Func to format the nth value in english"""
    try:
        return f"{val}{['st','nd','rd'][val-1]}"
    except IndexError:
        return f"{val}th"


## Allow user to add a fruits to the end of a list
def list_print_append(fruits=["Apples", "Pears", "Oranges", "Peaches"]):

    """ Series 1.a_b - Print and append to list"""
    while True:
        fruit = get_arg("Add a fruit to the end of the list")
        if fruit[0]:
            fruits.append(fruit[1])
            print(fruits)
        else:
            break

# list_print_append()

## Allow user to print the index of fruit in the list
def list_index(fruits=["Apples", "Pears", "Oranges", "Peaches"]):

    """Series 1.c Print an index of a list"""

    while True:
        print(fruits)
        fruit = get_arg("Enter a position in the fruit list")
        if fruit[0]:
            try:
                pos=int(fruit[1])

                assert pos-1 in range(len(fruits))

                print(f"The {ordinal(pos)} fruit in the list is \"{fruits[pos-1]}\"")

            except AssertionError:
                print(f"The available fruits are between 1 and {format(len(fruits))}")

            except ValueError:
                print(f"\"{format(fruit[1])}\" is not an integer!")
        else:
            break

# list_index()


# Add elements to the begining of the list
def list_prepend(fruits=["Apples", "Pears", "Oranges", "Peaches"]):

    """Series 1.d prepend elements to list """
    while True:
        print(fruits)
        fruit = get_arg("Enter a fruit to prepend to the existing fruit list")
        if fruit[0]:
            # Use the insert and concat operators
            if fruit[1].upper().startswith("A"):
                print("added with +")
                fruits=[fruit[1]]+fruits
            else:
                print("added with insert")
                fruits.insert(0,fruit[1])
        else:
            break

# list_prepend()

#display fruits that begin with letter
def list_startswith(fruits=["Apples", "Pears", "Oranges", "Peaches"]):

    """Series 1.e display fruits that start with a string"""

    while True:
        print(f"Available fruits: {fruits}")
        fruit = get_arg("Enter the string that begins the name of the desired fruits")
        if fruit[0]:
            display=[f for f in fruits if f.upper().startswith(fruit[1].upper())]
            print(f"Fruits that start with {fruit[1]}:" if len( display) > 0 else f"No fruits start with {fruit[1]}")
            if len(display):
                print("\n".join("\t" + str(p) for p in display))
        else:
            break

# list_startswith()

# Remove all the fruits that contain the search string
def list_remove_elements(fruits=["Apples", "Pears", "Oranges", "Peaches","Avocados","Pineapples","Pine cones"]):

    """" Series 2 - Remove elements from a list"""
    print(f"Available fruits: {fruits}")
    while True:

        fruit = get_arg("Remove fruit(s) from the list")
        if fruit[0]:
            bad_fruit=[f for f in fruits if f.upper().__contains__(fruit[1].upper())]

            if bad_fruit:
                confirm=get_arg(f"Are you sure you want to remove {bad_fruit} (Y/N)")

                if confirm[1].upper()=="Y":
                    fruits=[f for f in fruits if f not in bad_fruit]
                    print(f"New list includes: {fruits}")
            else:
                print("Try removing a fruit that exists")
        else:
            break

# list_remove_elements()



#Ask user if they like each fruit in the list and remove the No's
def list_remove(fruits=["Apples", "Pears", "Oranges", "Peaches","Grapes"]):

    """Series 3  - keep elements the user likes"""
    like=[]

    for i,ele in enumerate(fruits):
        resp=get_arg(f"Do you like {ele} (Y/N)?")
        if resp[0]:
            if (resp[1].upper().startswith("Y")):
                like.append(ele)
            else:
                print("Me neither :{")
        else:
            break

    print(f"Fruits you like: {like}")

# list_remove()



# Make a copy of the list and reverse the letters in each fruit in the copy.
# Delete the last item of the original list. Display the original list and the copy.

def list_reverse(fruits=["Apples", "Pears", "Oranges", "Peaches"]):

    """ Series 4: Reverse the elements in a list"""

    rev_fruits=[f[::-1] for f in fruits]
    print(rev_fruits)

    fruits.pop(-1)
    print(fruits)

list_reverse()



