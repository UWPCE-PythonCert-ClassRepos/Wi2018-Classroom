#mailroom program
#program needs to do the following: “Send a Thank You”, “Create a Report” or “quit”
#!/usr/bin/env python3

#initial list of donors
donor_db = {'Homer Simpson':[5,10,15],'Marge Simpson':[5,10,15],'Lisa Simpson':[5,10,15],'Bart Simpson':[5,10,15],'Maggie Simpson':[5,10,15]}

#get user menu choice as int
menu_choice = int(input("Please Choose From the Following Options:" + "\n" + "1 - Send a Thank You" + "\n" + "2 - Create a Report" + "\n" + "3 - Quit"))

def doer(menu_choice):
    if menu_choice == 1:
        get_donor()
        get_donation(donor_name)
    elif menu_choice ==2:
        print ("cool")
    else:
        print("need to exit here")

#Force lower then apply title caps to avoid errors
def get_donor():
    donor_name = input("Please Enter the Donor's Full Name:")
    donor_name = donor_name.lower().title()
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
        donor_name = input("Please Enter the Donor's Full Name:")
        donor_name = donor_name.lower().title()
        return donor_name

def get_donation(donor_name):
    donation = input("Please Enter the Donation Amount:")
    donation = int(donation)
    donor_db[donor_name] = donation
    return donation

#donor_name = get_donor()
#donation = get_donor()

doer(menu_choice)

print("this worked")
print(donor_name)
print(donor_db)
