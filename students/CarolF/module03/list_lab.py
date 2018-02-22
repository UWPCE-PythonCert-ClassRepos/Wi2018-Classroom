#!/usr/bin/env Python3


"""
####################################
## Week 3 list lab
## Created By: Carol Farris
## submitted: February 12th, 2018
##
####################################
"""

series1_list = ["Apples", "Pears","Oranges","Peaches"]

def makeList(l): #series 1 list tasks and calls Series 2 and 3
    """Completes tasks for series 1"""	
    print("Begin tasks for Series1_List_Activity//////////////////")
    fruityList = l
    print(fruityList)
    response = input("Please type in a fruit > ")
    fruityList.append(response)
    print(fruityList)
    numResponse = int(input("Please enter a whole number between 1 and 5: >"))

    while numResponse >= len(fruityList) or numResponse <= 0: 
        numResponse = int(input("Invalid entry! Please enter a whole number between 1 and 5: >"))
        list_indexing = numResponse
    if numResponse >0:
    	list_indexing = numResponse -1 

    print("You entered: ", numResponse, ", which corresponds to ", fruityList[list_indexing])
    fruityList = ["Watermelon"] + fruityList
    print(fruityList)
    fruityList.insert(0,"Pumello")
    print(fruityList)

    for each in fruityList:
        if (each.startswith("P")):
            print(each) 

    print("Begin tasks for Series2_List_Activity//////////////////")
    displayList(fruityList)
    print("Begin tasks for Series3_List_Activity//////////////////")
    userDelPreferences(fruityList)			


def displayList(alist): #series 2 list tasks
    """"Uses list created from makeList method, removes last value, prints result, asks user to provide a fruit to delete and removes it."""	
    listToModify = alist
    print(listToModify)
    listToModify.pop()
    print(listToModify)
    usrFruit = str(input("Pick a fruit to delete from above list >")) 
    while (usrFruit not in  listToModify): #will ensure user provides a value from the list
        usrFruit = str(input("Invalid!!! Pick a fruit to delete from above list. Input is case sensitive. >"))

    listToModify.remove(usrFruit)
    print(listToModify)	#prints the final list
    

def reverseAndDelete(listToEdit): #series 4 list tasks
    """Makes a copy of list generated in userDelPreferences and reverses the letters in each frut in the copy, deletes the last original item"""
    print("Begin tasks for Series4_List_Activity//////////////////")
    staticList =[]
    staticList.extend(listToEdit) #created static list to keep original values of the list before modifying below.
    listToModify = listToEdit
    lastItem = listToModify[(len(listToModify)-1)]
    for fruit in listToModify:
        reverseFruit = fruit[::-1]
        listToModify[listToModify.index(fruit)] = reverseFruit
    staticList.pop()    
    print("original list with last value removed: ", staticList)
    print("Modified list, last value included: ",listToModify)
    

def userDelPreferences(blist):  #series 3 list tasks
    """Cycles through list created by previous methods and asks user whether they like the fruit. If they don't the fruit is removed fromlist."""
    listToEdit = blist
    hatedList = []
    for fruit in listToEdit: ## Need to switch to i in len(listToEdit), once you delete
        likesFruit = str(input("Do you like " + fruit.lower() + "? Please enter 'yes' or 'no' >"))
           
        while (likesFruit.lower() != "yes" and likesFruit.lower() != "no" ):
            likesFruit = str(input("Invalid Entry! Please type either a'yes' or a'no'. Do you like " + fruit.lower() + "? >"))

        if (likesFruit.lower() == "no"):
            hatedList.append(fruit)

    for fruit in hatedList:
        listToEdit.remove(fruit)
    
    print("initial list with disliked fruits removed: ", listToEdit)  
    reverseAndDelete(listToEdit)



if __name__ == "__main__" :
    series1_list = ["Apples", "Pears","Oranges","Peaches"]
    makeList(series1_list)

######################################################







