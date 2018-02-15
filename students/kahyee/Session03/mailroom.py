
donationList = [["Bob", 1.00, 2.00],["Jon", 1.50, 100.00],["Sally",1000.00],["Barry", 50.00],["Ellen", 1.25]]

def CreateReport():
	print("Donor Name          | Total Given | Num Gifts | Average Gift")
	print("------------------------------------------------------------")
	for donor in donationList:
		giftCount = str(len(donor) - 1)
		giftTotal = "%.2f" % sum(donor[1:])
		giftAvg = "%.2f" % (sum(donor[1:]) / len(donor))
		print(donor[0] \
			+ " " * (20 - len(donor[0])) \
			+ " $" + " " * (12 - len(giftTotal)) + giftTotal \
			+ " " * 10 + str(giftCount) \
			+ " $" + " " * (12 - len(giftAvg)) + giftAvg)


def ThankYou():
    donorName = input("Donor's Full Name: ")
    exist = False
    while donorName == "list":
        for donor in donationList:
            print(donor[0])
        donorName = input("Donor's Full Name: ")
    donationAmt = float(input("How much did they donate?"))
    for donor in donationList:
        if donor[0] == donorName:
            donor.append(donationAmt)
            exists = True
            break
    if not exist:
        donationList.append([donorName, donationAmt])
    email(donorName)

  
def email(donorName):
	print("\nDear " + donorName + "," + \
  	"\n\n Thank you for your generous donation."+ \
  	"Your kindness knows no bounds. Yada yada yada." + \
  	"Please send more money soon \n\n Best, \n Kahyee \n")
    
      

userPrompt = input("Select Action \n 1. Send a Thank You \n 2. Create a Report \n 3. quit \n")


while userPrompt != "3":

  if userPrompt == "1":
  	ThankYou()
  elif  userPrompt == "2":
    CreateReport()
    
  userPrompt = input("Select Action \n 1. Send a Thank You \n 2. Create a Report \n 3. quit \n")