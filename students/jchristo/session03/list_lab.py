#List Lab
#!/usr/bin/env python3

"""
Series 1
Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
Display the list (plain old print() is fine…).
Ask the user for another fruit and add it to the end of the list.
Display the list.
Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
Add another fruit to the beginning of the list using “+” and display the list.
Add another fruit to the beginning of the list using insert() and display the list.
Display all the fruits that begin with “P”, using a for loop.
"""

def list_lab_s1():
    fruit_list = ["Apples","Pears","Oranges","Peaches"]
    print (fruit_list)
    response = input("Please add any type of fruit to the list: ")
    fruit_list.append(response)
    print (fruit_list)
    response_2 = input("Please enter a number: ")
    print ("You entered the number " + response_2 +", which is the following fruit in the list: " +fruit_list[int(response_2)])
    print (["Kiwi"] + fruit_list)
    fruit_list.insert(0,"Grapes")
    print (fruit_list)
    for i in fruit_list:
        if "P" in i:
            print (i)
