import os

donation_dict = {
"Bob": [1.00, 2.00],
"Jon": [1.50, 100.00],
"Sally": [1000.00], 
"Barry": [50.00],
"Ellen": [1.25]
}

def create_report():
	print("Donor Name          | Total Given | Num Gifts | Average Gift")
	print("------------------------------------------------------------")
	for donor, amounts in donation_dict.items():
		gift_count = str(len(donor) - 1)
		gift_total = "%.2f" % sum(amounts)
		gift_avg = "%.2f" % (sum(amounts) / len(donor))
		print(donor \
			+ " " * (20 - len(donor)) \
			+ " $" + " " * (12 - len(gift_total)) + gift_total \
			+ " " * 10 + str(gift_count) \
			+ " $" + " " * (12 - len(gift_avg)) + gift_avg)


def thank_you():
    donor_name = input("Donor's Full Name: ")
    exist = False
    while donor_name.lower() == "list":
        [print(donor) for donor in donation_dict.keys()]
        donor_name = input("Donor's Full Name: ")
    donation_amt = float(input("How much did they donate?"))
    for donor, amounts in donation_dict.items():
        if donor == donor_name:
            amounts.append(donation_amt)
            exists = True
            break
    if not exist:
        donation_dict[donor_name] = [donation_amt]
    print(email(donor_name, donation_amt))

  
def email(donor_name, amt):
	return "\nDear " + donor_name + "," \
  	    + "\n\n Thank you for your generous donation of $" + '%.2f' % amt \
  	    + " Your kindness knows no bounds. Yada yada yada." \
  	    + "Please send more money soon \n\n Best, \n Kahyee \n"

def default_prompt():
    return int(input("Select Action \n 1. Send a Thank You \n 2. Create a Report \n 3. Send Letters to Everyone \n 4. Quit \n"))    
      
def all_email():
  for donor, amounts in donation_dict.items():
    thank_you_letter = open(os.getcwd() + '/' + donor + '.txt', 'w+')
    thank_you_letter.write(email(donor, amounts[-1]))
    thank_you_letter.close()

user_prompt = default_prompt()


switch_prompt_dict = {
  1: thank_you,
  2: create_report,
  3: all_email
}

while user_prompt != 4:
  if user_prompt in [1, 2, 3]:
    switch_prompt_dict[user_prompt]()
    
  user_prompt = default_prompt()