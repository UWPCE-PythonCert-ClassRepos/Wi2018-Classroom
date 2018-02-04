
donors = [["Allen, Paul", [1000000, 50000, 300000]], 
                    ["Gates, Bill", [5000000, 80000, 700000]], 
                    ["Bezos, Jeff", [30000]], 
                    ["Musk, Elon", [1000000, 30000]], 
                    ["Zuckerberg, Mark",[10000, 50000, 12000, 400000]]]

donor_sort = sorted(donors, key=lambda donor: sum(donor[1]), reverse=True)
#print(donor_sort)

def make_report(donor):
    col_names = ["Donor Name", "| Total Given", "| Num Gifts", "| Average Gift"]
    headers = f'{col_names[0]:20}{col_names[1]:>15}{col_names[2]:^15}{col_names[3]:20}'
    print(headers)
    print(("_")*65)
    print((" "))
    for n in range(len(donors)):
        columns = f'{(donor[n])[0]:20}{sum((donor[n])[1]):15}{len((donor[n])[1]):^15}{(sum((donor[n])[1])/len((donor[n])[1])):12.2f}'
        print(columns)
make_report(donor_sort)


def show_list():
    abc_sort = (sorted(donors, key=lambda donor: donor[0]))
    for n in range(len(abc_sort)):
        print((abc_sort[n])[0])


def thank_you_email():
    

def init_prompt():
    init_response = input("What do you want to do?")
    if init_response == "list":
        show_list()
        init_prompt()
    elif init_response == 1:
        thank_you_email()
    #return init_response
init_prompt()




'''
init_prompt = input("Would you like to, 1 Send a Thank You, 2 Create a Report, or 3 quit?")
if init_prompt == 1:
    name_prompt = input("Please enter a name: ")
    if name_prompt in donors:
        donation_prompt = input("Please enter a donation amount: ")
    else:
        donors.append(name_prompt)
        donation_prompt = input("Please enter a donation amount: ")
elif init_prompt == "list":
    abc_sort = (sorted(donors, key=lambda donor: donor[0]))
    print(abc_sort)
    for n in range(len(abc_sort)):
        print((abc_sort[n])[0])
'''
    #name_prompt 

