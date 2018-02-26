#!/usr/bin/env python3




if __name__ == '__main__':

    # Series 1
    my_list = ['Apples', 'Pears', 'Oranges', 'Peaches']

    # Display the list
    print(my_list)

    # Prompt user for fruit to add to list
    response = input("Please enter another fruit to add to the list: ")

    my_list.append(response)

    # Display the list again
    print(my_list)

    while not response.isdigit():
        response = input(
            "Give me a number and I'll return that fruit in the list (or <Enter> to skip): ")
        if not response:
            break

    try:
        print(my_list[int(response) - 1])
    except:
        # Cannot print if user broke out of above loop or if the index
        # is out of range
        print("Whoops, can't find that fruit!")
        pass
    
    my_list = ['Cherry'] + my_list
    print(my_list)
    my_list.insert(0, 'Kiwi')
    print(my_list)

    for fruit in my_list:
        if fruit[0].lower() == 'p':
            print(fruit)

    # Series 2
    
