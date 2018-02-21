#mailroom program
#program needs to do the following: “Send a Thank You”, “Create a Report” or “quit”
#!/usr/bin/env python3

#for saving files to user desktop
import os

#initial list of donors
donor_db = {'Homer Simpson':[5,10,50],'Marge Simpson':[5,20,100],\
            'Lisa Simpson':[10,30,65],'Bart Simpson':[15,55,500],\
            'Maggie Simpson':[5,70,50]}

#add exception handling
def user_prompt():
    menu_choice = int(input(f"Please Choose From the Following Options: \n 1 - Send a Thank You \n 2 - Create a Report \n "
                            f"3 - Send Letters to Everyone \n 4 - Quit"))
    while menu_choice != 4:
        doer(menu_choice)
        menu_choice = int(input(f"Please Choose From the Following Options: \n 1 - Send a Thank You \n 2 - Create a Report \n "
                            f"3 - Send Letters to Everyone \n 4 - Quit"))
    return menu_choice

def doer(menu_choice):
    if menu_choice == 1:
        get_donor()
        get_donation(donor_name)
        write_note(donor_name,donation)
    elif menu_choice ==2:
        create_report()
    elif menu_choice == 3:
        send_letters()

#Force lower then apply title caps to avoid errors, need to add exception handling
def get_donor():
    global donor_name
    donor_name = input("Please Enter the Donor's Full Name:").lower().title()
    if donor_name != "List":
        if donor_name in donor_db.keys():
            print("Existing Donor")
            return donor_name
        elif donor_name not in donor_db.keys():
            donor_db[donor_name] = []
            print("New Donor")
            return donor_name
    elif donor_name == "List":
        print(donor_db.keys())
        donor_name = input("Please Enter the Donor's Full Name:").lower().title()
        if donor_name in donor_db.keys():
            print("Existing Donor")
            return donor_name
        elif donor_name not in donor_db.keys():
            donor_db[donor_name] = []
            print("New Donor")
            return donor_name

#need to add exception handling
def get_donation(donor_name):
    global donation
    donation = int(input("Please Enter the Donation Amount:"))
    donor_db[donor_name].append(donation)
    #global total_donation
    #total_donation = sum(donor_db[donor_name])
    return donation

def write_note(donor_name,donation):
    print(f"Thank You {donor_name} for Your Generous Donation of: ${donation}")

def create_report():
    print("Donor Name "+""*4+"| Total Given | "+""*4+"Num of Gifts | "+""*4+"Avg Gift"+ "\n" + "-"*50)
    for k,v in sorted(donor_db.items(),key=lambda i:sum(i[1]),reverse=True):
        #need to figure out how to print avg as float in the code below
        print("{:<} ${:>10} {:>10} ${:>}".format(k,sum(v),len(v),(sum(v)/len(v))))

#save location does not work with desktop when used
def send_letters():
    for donor in donor_db:
        file_name = f"{donor.replace(' ','_')}.txt"
        letter_location = os.path.join(os.path.expanduser("~"),file_name)
        total_donation = sum(donor_db[donor])
        letter_contents = f"Dear {donor}, \n Thank you for your very kind donation of {total_donation}. \n " \
                          "It will be put to very good use \n Sincerely, \n The Team"
        with open(letter_location,"w") as f:
            f.write(letter_contents)
    print("Letter Generation Complete")

user_prompt()

print("Exiting")
