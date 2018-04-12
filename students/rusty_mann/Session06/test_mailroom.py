#!/usr/bin/env python3

import os
import mailroom_session06 as mr


def test_make_donor_list():
    assert mr.make_donor_list() == ["Allen, Paul", "Bezos, Jeff", "Gates, Bill", "Musk, Elon", "Zuckerberg, Mark"]


def test_get_donor():
    assert mr.get_donor("Allen, Paul") == "Allen, Paul"
    assert mr.get_donor("Mann, Rusty") == None


def test_make_letter_files():
    assert os.path.isfile('Allen_Paul.txt')
    with open('Allen_Paul.txt') as f:
        size = len(f.read())
    assert size > 0


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


def test_make_report():
    report = mr.make_report()
    print(report)
    assert report.startswith("Donor Name          |  Total Given |  Num Gifts  |  Average Gift\n")
    assert "Gates, Bill          $  5780200.00       5         $ 1156040.00" in report

