from mailroom_part4 import *

def test_initializeDonorDB():
	assert initializeDonorDB() == {"Navdeep Gill": [1000], "Nick Garzon": [5,2], "Henry Chipman":[100], 
	"Lorenzo B": [1000], "Torin Stetina": [200.75]}

def test_initializeOptionsDB():
	assert initializeOptionsDB() == {'t': askUserForDonor, 's': createFileName, 'r': createReport, 'e': exitMessage}


def test_displayMenu():
	assert displayMenu().startswith("1. Type 't'")
	assert displayMenu().endswith("the program")

def test_menu():
	donors = {"Navdeep Gill": [1000], "Nick Garzon": [5,2], "Henry Chipman":[100], "Lorenzo B": [1000], "Torin Stetina": [200.75]}
	menu_db = {'t': askUserForDonor, 's': writeToFile, 'r': createReport, 'e': exitMessage}
	assert menu(donors, menu_db) == 't'

def test_askUserForDonor():
    donors = {"Navdeep Gill": [1000], "Nick Garzon": [5,2], "Henry Chipman":[100], "Lorenzo B": [1000], "Torin Stetina": [200.75]}
    assert askUserForDonor(donors) == "addNewDonor(donor_dict)"


def test_donorExists():
	donors = {"Navdeep Gill": [1000], "Nick Garzon": [5,2], "Henry Chipman":[100], "Lorenzo B": [1000], "Torin Stetina": [200.75]}
	assert donorExists(donors, "Navdeep Gill") == True
	assert donorExists(donors, "Kaleb Smith") == False

def test_showDonorNames():
	donors = {"John Smith" : [100], "Jane Doe": [200]}
	assert showDonorNames(donors) == ["John Smith", "Jane Doe"]	

def test_addNewDonor():
	donors = {"John Smith" : [100], "Jane Doe": [200]}
	assert addNewDonor(donors) == "Kelly Pratt"

def test_addNewDonation():
	donors = {"John Smith" : [100], "Jane Doe": [200]}
	assert addNewDonation(donors, "Kelly Pratt") == {"John Smith" : [100], "Jane Doe": [200], "Kelly Pratt":[1000]}

def test_sum():
	list_sum = [1,2,3]
	assert calculateSum(list_sum) == 6

def test_average():
	list_average = [1,2,3]
	assert calculateAverage(list_average) == 2

def test_reportHeader():
	assert reportHeader().startswith("Donor Name")
	assert "Total Given" in reportHeader()
	assert "Num Gifts" in reportHeader()
	assert "Average Gift" in reportHeader()

def test_createReport():
	donors = {"John Smith" : [100], "Jane Doe": [200]}
	assert createReport(donors) == {"John Smith": [100, 1, 100], "Jane Doe": [200, 1, 200]}

def test_printReport():
	donors = {"John Smith" : [200, 2, 100]}
	assert "John Smith" in printReport(donors)
	assert "200" in printReport(donors)
	assert "2" in printReport(donors)
	assert "100" in printReport(donors)

def test_thank_you_message():
	new_donor = "John Smith"
	newest_donation = 100
	assert "John Smith" in printThankYou(new_donor, newest_donation)
	assert "100" in printThankYou(new_donor, newest_donation) 

def test_letterToSend():
	new_donor = "Navdeep Gill"
	donations = [100,200]
	assert letterToSend(new_donor, donations).startswith("Dear Navdeep Gill")
	assert "100" in letterToSend(new_donor, donations)
	assert "200" in letterToSend(new_donor, donations)

def test_createFileName():
	donors = {"John Smith": [100]}
	assert createFileName(donors) == "John_Smith.txt"

def test_writeToFile():
	with open("Navdeep_Gill.txt") as f:
		size = len(f.read())
	assert size > 0

def test_exitMessage():
	donors = {"Navdeep Gill": [1000], "Nick Garzon": [5,2], "Henry Chipman":[100], 
	"Lorenzo B": [1000], "Torin Stetina": [200.75]}
	assert exitMessage(donors).startswith("Thank you to the following donors")
	assert "Nick Garzon" in exitMessage(donors)


