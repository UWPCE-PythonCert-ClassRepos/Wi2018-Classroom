
## Class 03: Series 1 & 2
def list_series1(fruits=["Apples", "Pears", "Oranges", "Peaches"]):

    # print(fruits)
    #
    # more_fruit=input("Add some fruit > ")
    #
    # if more_fruit:
    #     fruits.append(more_fruit)
    #
    #     print(fruits)
    #
    # # prompt for a valid position in the fruit list
    # pos=0
    # #
    # while not (1 <= pos < len(fruits) + 1):
    #     pos = int(input("Enter fruit number > "))
    #
    #     if not (1 <= pos < len(fruits) + 1):
    #         print("Numbers between 0 and {}".format(len(fruits)))
    #
    # else:
    #     print("Position {} is  {}".format(pos, fruits[pos - 1]))
    #
    # # Add some fruit to the begining of the list
    # more_fruit = input("Prepend some more fruits > ")
    # if more_fruit:
    #     fruits.append(more_fruit)
    # while more_fruit:
    #     more_fruit = input("Prepend some more fruits > ")
    #
    #     if more_fruit:
    #         fruits.append(more_fruit)
    # else:
    #     print("Fruit list includes: {}".format(fruits))
    #
    # # fruits that start with P
    # p_fruit=[f for f in fruits if f.upper().startswith('P')]
    #
    # print("Fruits that start with 'P':")
    # for f in p_fruit:
    #     print('\t'+f)

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

# list_series3()

