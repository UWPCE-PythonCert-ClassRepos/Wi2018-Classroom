
## Series 1
def list_series1(list=["Apples","Pears","Oranges","Peaches"]):

    # print(list)

    # more_fruit=input("Add some fruit > ")
    #
    # if more_fruit:
    #     list.append(more_fruit)
    #
    #     print(list)
    #
    # pos=0
    # while not (1<= pos <len(list)+1 ):
    #     pos = int(input("Enter fruit number > "))
    #
    #     if not (1<= pos <len(list)+1):
    #         print("Numbers between 0 and {}".format(len(list)))
    #
    # else:
    #     print("Position {} is  {}".format(pos, list[pos-1]))

    more_fruit = input("Prepend some more fruits > ")
    if more_fruit:
        list.append(more_fruit)
    while more_fruit:
        more_fruit = input("Prepend some more fruits > ")

        if more_fruit:
            list.append(more_fruit)
    else:
        print("Fruit list includes: {}".format(list))

    # p_fruit=[f for f in list if f[0].upper() == 'P']
    #
    # print("Fruits that start with 'P':")
    # for f in p_fruit:
    #     print('\t'+f)

    counter=0
    while True:

        if counter:
            del_fruit=input("Try again, remove a fruit that exists >")
        else:
            del_fruit=input("Remove a fruit >")

        rem_fruit=[f for f in list if f.upper() == del_fruit.upper()]
        counter+=1
        if rem_fruit:
            for f in rem_fruit:
                list.remove(f)

                print("Removing {}".format(f))
            break








list_series1()
