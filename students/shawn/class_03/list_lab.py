
## Class 03: Series 1 & 2
def list_series1(fruits=["Apples", "Pears", "Oranges", "Peaches"]):

    print(fruits)

    more_fruit=input("Add some fruit > ")

    if more_fruit:
        fruits.append(more_fruit)

        print(fruits)

    # prompt for a valid position in the fruit list
    position=0
    raw=""
    while True:
        try:
            raw=input("Enter fruit number > ")
            position = int(raw)
            assert position-1 in range(len(fruits))
            break

        except AssertionError:
            print("Numbers between 1 and {}".format(len(fruits)))

        except ValueError as e:
            print("\"{}\" is not an integer!".format(raw))

    print("Position {} is  {}".format(position, fruits[position - 1]))



    # Add some fruit to the begining of the list
    more_fruit = input("Prepend some more fruits > ")
    if more_fruit:
        fruits.insert(0,more_fruit)
    while more_fruit:
        more_fruit = input("Prepend some more fruits > ")

        if more_fruit:
            fruits.insert(0,more_fruit)
    else:
        print("Fruit list includes: {}".format(fruits))

    # fruits that start with P
    p_fruit = [f for f in fruits if f.upper().startswith('P')]

    print("Fruits that start with 'P':")
    for f in p_fruit:
        print('\t'+f)

    # remove fruits from the list
    counter=0
    while True:

        if counter:
            del_fruit=input("Try again, remove a fruit that exists >")
        else:
            del_fruit=input("Remove a fruit >")

        rem_fruit=[f for f in fruits if f.upper() == del_fruit.upper()]
        counter+=1
        if rem_fruit:
            for f in rem_fruit:
                fruits.remove(f)

                print("Removing {}".format(f))

            break


list_series1()

## Class 03 Series 3
def list_series3(list = ["apples", "Bananas", "Pears"]):
    rm = []
    for i in list:
        is_valid = 0
        while not is_valid:

            is_like=input("Do you like {}?(y/n): ".format(i))
            if is_like.upper() in ("Y","N"):
                is_valid = 1

                if (is_like.upper() == "N"):
                    rm.append(i)

    for i in rm:
        list.remove(i)

    print("New List: {}".format(list))

list_series3()

## Class 03 Series 4
# Make a copy of the list and reverse the letters in each fruit in the copy.
# Delete the last item of the original list. Display the original list and the copy.

def list_series4(fruits=["Apples", "Pears", "Oranges", "Peaches"]):

    rev_fruits=[f[::-1] for f in fruits]
    print(rev_fruits)

    fruits.pop(-1)
    print(fruits)

list_series4()



