#!/usr/bin/env python3

donation_db = ["Rob Royal",[1090.89,878.67,789.90],"Richie Rich",[560.02,434.05],"Ashton Average",[120.03,98.53],"Paul Poor",[10.03],"Joe Jobless",[1.03,2.04]]
user_choice=''

while user_choice != '3':
    user_choice = input("Key 1 to 'Send a Thank You', 2 to 'Create a Report' or 3 to 'Quit' > ")

    if user_choice == '1':
        user_input_name = input("Key donor's full name (key 'quit' to return to original prompt) > ")
        if user_input_name == 'quit':
            continue
        while user_input_name =='list':
            for i in range(0,len(donation_db),2):
                print(donation_db[i],end="\n")
            user_input_name = input("Key donor's full name (key 'quit' to return to original prompt) > ")
            if user_input_name == 'quit':
                continue
        if user_input_name in donation_db:
            for i in range(0,len(donation_db),2):
                if user_input_name==donation_db[i]:
                    user_input_donation=input("Key donation amount (key 'quit' to return to original prompt) > ")
                    if user_input_donation == 'quit':
                        continue
                    donation_db[i+1].append(float(user_input_donation))
                    print("Hi {},\n\nThank you for your generation donation of ${}!\n\nYour sincerely,\nCharity Trust".format(donation_db[i],user_input_donation))
        else:
            if user_input_name == 'quit':
                continue
            donation_db.append(user_input_name)
            donation_db.append([])
            user_input_donation=input("Key donation amount (key 'quit' to return to original prompt) > ")
            if user_input_donation == 'quit':
                donation_db.pop()
                donation_db.pop()
                continue
            donation_db[len(donation_db)-1].append(float(user_input_donation))
            print("Hi {},\n\nThank you for your generation donation of ${}!\n\nYour sincerely,\nCharity Trust".format(user_input_name,user_input_donation))

    if user_choice=='2':
        Heading = "Donor Name          | Total Given | Num Gifts | Average Gift"
        print(Heading)
        print("-"*len(Heading))
        for i in range(0,len(donation_db),2):
            print("{}{}${}{}   {} {}  ${}{}".format(donation_db[i],
                ' '*(21-len(donation_db[i])),
                ' '*(11-len(str(round(sum(donation_db[i+1]),2)))),
                round(sum(donation_db[i+1]),2),
                ' '*(8-len(str(len(donation_db[i+1])))),
                len(donation_db[i+1]),
                ' '*(12-len(str(round((sum(donation_db[i+1])/len(donation_db[i+1])),2)))),
                round((sum(donation_db[i+1])/len(donation_db[i+1])),2)))