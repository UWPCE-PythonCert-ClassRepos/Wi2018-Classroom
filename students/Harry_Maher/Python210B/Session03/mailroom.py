#!/usr/bin/env python3
'''
You work in the mail room at a local charity. Part of your job is to write incredibly boring, repetitive emails thanking your donors for their generous gifts. You are tired of doing this over and over again, so you’ve decided to let Python help you out of a jam and do your work for you.
The program

Write a small command-line script called mailroom.py. This script should be executable. The script should accomplish the following goals:

    It should have a data structure that holds a list of your donors and a history of the amounts they have donated. This structure should be populated at first with at least five donors, with between 1 and 3 donations each.

    You can store that data structure in the global namespace.

    The script should prompt the user (you) to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”)


if the user (you) selects ‘Send a Thank You’, prompt for a Full Name.

    If the user types ‘list’, show them a list of the donor names and re-prompt
    If the user types a name not in the list, add that name to the data structure and use it.
    If the user types a name in the list, use it.
    Once a name has been selected, prompt for a donation amount.
    Turn the amount into a number – it is OK at this point for the program to crash if someone types a bogus amount.
    Once an amount has been given, add that amount to the donation history of the selected user.
    Finally, use string formatting to compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.


    If the user (you) selected “Create a Report”, print a list of your donors, sorted by total historical donation amount.
        Include Donor Name, total donated, number of donations and average donation amount as values in each row. You do not need to print out all their donations, just the summary info.
        Using string formatting, format the output rows as nicely as possible. The end result should be tabular (values in each column should align with those above and below)
        After printing this report, return to the original prompt.
    At any point, the user should be able to quit their current task and return to the original prompt.
    From the original prompt, the user should be able to quit the script cleanly.

Your report should look something like this:

Donor Name                | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------
William Gates, III         $  653784.49           2  $   326892.24
Mark Zuckerberg            $   16396.10           3  $     5465.37
Jeff Bezos                 $     877.33           1  $      877.33
Paul Allen                 $     708.42           3  $      236.14



'''

donors = ["Bill", "Bob", "Jim", "Ann", "Beth"]
amounts = [2.53,46.12,3.12,56.11,7.33]
num_gifts = [1,2,1,1,1]

choice =" "
def mailroom():
    """automates mail sending and report generation """
    choice =" "
    while choice != "3":
        choice = input("Pick a number: \n1. Send thank you \n2. Create report \n3. Quit\n")
        if choice == "1":
            name = input("Pick or add a name!\n").lower()
            if name == "list":
                print(donors)
                name = input("Pick or add a name!")
            if name not in donors and (name !="list"):
                donors.append(name)
                amounts.append(0)
                num_gifts.append(0)
            donation = input("How much did they donate?\n")
            amounts[donors.index(name)]+=float(donation)
            num_gifts[donors.index(name)]+=1
            print("Dear {0},\n \tThanks so much for your generous donation of ${1:.2f}. We are all incredibly grateful because without you blah blah blah! \n-NGO".format(name, amounts[donors.index(name)]))

        if choice == "2":
            print("{:16}|{:^13}|{:^11}|{:>13}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
            for donor in donors:
                print("{:17}${:>12} {:>10} ${:>12}".format(donor, amounts[donors.index(donor)], num_gifts[donors.index(donor)],(amounts[donors.index(donor)]/num_gifts[donors.index(donor)])))



if __name__ == "__main__":
    mailroom()
