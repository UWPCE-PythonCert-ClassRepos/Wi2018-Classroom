#!/usr/bin/env python3

import mailroom_session06 as mr


def test_make_donor_list():
    assert mr.make_donor_list() == ["Allen, Paul", "Bezos, Jeff", "Gates, Bill", "Musk, Elon", "Zuckerberg, Mark"]
    #assert "Allen, Paul" in donor_list


def test_get_donor():
    assert mr.get_donor("Allen, Paul") == "Allen, Paul"
    assert mr.get_donor("Mann, Rusty") == None


def test_split_name():
    assert mr.split_name("Gates, Bill") == ('Bill', 'Gates')


def test_donor_dict():
    assert mr.make_donor_dict("Allen, Paul", 10.0) == {"first name": "Paul",
     "last name": "Allen", "amt": 10.0}


def test_add_donor():
    mr.add_donor("Allen, Paul", 10) 
    assert 10 in mr.donor_data["Allen, Paul"]
    mr.add_donor("Mann, Rusty", 100)
    assert 100 in mr.donor_data["Mann, Rusty"] 


def test_donor_selection():
    assert mr.donor_selection("mann, rusty") == "Mann, Rusty"
    assert mr.donor_selection("allen paul") == "Allen Paul"


def test_get_donor_name():
    assert mr.get_donor_name("Mann, Rusty") == "Mann, Rusty"
    assert mr.get_donor_name("Menu") == None
    #mr.get_donor_name("List")
    #assert 
    #assert mr.get_donor_name("LIST") == print('List of donors:', 'Allen, Paul', 'Bezos, Jeff', 'Gates, Bill', 'Musk, Elon', 'Zuckerberg, Mark')
    #with break statement at line 123 to stop loop
    #assert mr.get_donor_name("Allen Paul") == print("Error: Please enter a last name and first name seperated by a comma!")


def test_donation_selection():
    assert mr.donation_selection(100) == "100"
    assert mr.donation_selection("money") == "money"


def test_get_donation_amount():
    assert mr.get_donation_amount("mEnu") == None
    #with break statement to stop loop
    #assert mr.get_donation_amount("money") == print("Error: Please enter a number")
    assert mr.get_donation_amount("100") == 100.0


def test_send_donor_email():
    #mr.send_donor_email("Gates, Bill", 100.0)
    assert "Bill Gates" in mr.send_donor_email ("Gates, Bill", 100.0)
    assert "$100.00" in mr.send_donor_email("Gates, Bill", 100.0)

#def test_get_donor_name():
    #with "Menu" passed as input
    #assert mr.get_donor_name() == None
    #with "LIST " passed as input
    #assert mr.get_donor_name() == print(["Allen, Paul",
    #"Bezos, Jeff", "Gates, Bill", "Musk, Elon", "Zuckerberg, Mark"])
    #with "mann rusty" passed as input
    #assert mr.get_donor_name() == None #print("Error: Please enter a last name and first name seperated by a comma!")
    #with "mann, rusty" passed as input
    #assert mr.get_donor_name() == "Mann, Rusty"


#def test_send_donor_email():
    #with "mann, rusty" and "100" passed as inputs
    #assert mr.send_donor_email() == print('''\n
        #Dear Rusty Mann, 
        #Thank you for your donation of $100.00.
        #You are a good person.
                            #Sincerely,
                            #-Me''')
