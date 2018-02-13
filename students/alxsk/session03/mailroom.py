'''
Write a small command-line script called mailroom.py. This script should be executable. The script should accomplish the following goals:


'''
print("Welcome to the mailroom. Below is the current donor list")
print()

#Donor List
donor_list= [['Alis',500,350,400],['Neha', 1000, 3452,431,333],['Mohan', 780,570],['Sree', 1500],['Yash',800]]

#parse 
for row in donor_list:
	for element 

#Printing the donor list
for row in donor_list:
    for elem in row:
        print(elem, end=' ')
    print()
print()

#Input prompting user pick one of 3 actions: “Send a Thank You”, “Create a Report” or “quit”

prompt=input("Send a Thank You, create a report, quit program: ")

if prompt== "Send a Thank You":
	name_prompt=input('Select a name: ')
		if name_prompt=


'''
If the user (you) selects ‘Send a Thank You’, prompt for a Full Name.
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
'''