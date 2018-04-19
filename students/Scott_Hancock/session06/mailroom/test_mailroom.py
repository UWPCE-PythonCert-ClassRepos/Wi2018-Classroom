import mailroom

db = mailroom.getDonorDB()

def test_add_donor():
    name = "Fred Flintstone "

    donor = mailroom.Donor(name)
    donor.addDonation(300)
    db.addDonor(donor)
    assert donor.name == "Fred Flintstone"
    assert donor.donationList == [300]
    assert db.findDonor(name) == donor

def test_find_donor():
    db.addDonor(mailroom.Donor("Bill Gates"))
    assert db.findDonor("  Bill GaTes\n").name == "Bill Gates"

def test_find_donor_not():
    db.addDonor(mailroom.Donor("Bill Gates"))
    assert db.findDonor("Bill Gtes") is None

def test_add_donation():
    donationamt = 10000.00
    db.findDonor("Bill Gates").addDonation(donationamt)
    assert db.findDonor("Bill Gates").donationList[-1:][0] == donationamt

def test_num_donations():
    donor = mailroom.Donor("Zhou Qunfei")
    donor.addDonation(5000.00)
    donor.addDonation(15000.00)
    donor.addDonation(11000.00)
    db.addDonor(donor)
    assert db.findDonor("Zhou Qunfei").getNumDonations() == 3

def test_avg_donation():
    donor = mailroom.Donor("Mark Zuckerberg")
    donor.addDonation(5000.00)
    donor.addDonation(15000.00)
    db.addDonor(donor)
    assert db.findDonor(" mark zuckerberg ").getAvgDonation() == 10000.00

def test_tot_donation():
    donor = mailroom.Donor("Marian Ilitch")
    donor.addDonation(5000.00)
    donor.addDonation(15000.00)
    db.addDonor(donor)
    assert db.findDonor(" marian ilitch ").getTotDonation() == 20000.00

def test_create_thank_you_email():
    name = "Test"
    donor = mailroom.Donor(name)
    donor.addDonation(5000.00)
    db.addDonor(donor)
    assert db.findDonor("Test").createThankYouEmail() == ("\nDear Test,\n\n"
        "\tThank you so much for your generous donation of $5,000.00!\n\n"
        "\tIt will be put to very good use.\n\n"
        "\t\tSincerely,\n\t\t\t- The Team")

if __name__ == '__main__':
    test_add_donor()
    test_find_donor()
    test_find_donor_not()
    test_add_donation()
    test_num_donations()
    test_avg_donation()
    test_tot_donation()
    test_create_thank_you_email()