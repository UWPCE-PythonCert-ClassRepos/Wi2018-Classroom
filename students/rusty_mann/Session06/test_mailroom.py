#!/usr/bin/env python3

import mailroom_session06 as mr


def test_1():
    assert mr.show_donor_list() == print(["Allen, Paul",
     "Bezos, Jeff", "Gates, Bill", "Musk, Elon", "Zuckerberg, Mark"])


def test_2():
    assert mr.get_donor("Allen, Paul") == "Allen, Paul"
    assert mr.get_donor("Mann, Rusty") == None


def test_split_name():
    assert mr.split_name("Gates, Bill") == ('Bill', 'Gates')


def test_donor_dict():
    assert mr.make_donor_dict("Allen, Paul", 10.0) == {"first name": "Paul",
     "last name": "Allen", "amt": 10.0}


def test_add_donor():
    assert mr.add_donor("Allen, Paul", 10) == {"Allen, Paul": [1000000.00, 50000.00, 300000.00, 10],
                    "Gates, Bill": [5000000.00, 80000.00, 700000.00],
                    "Bezos, Jeff": [30000.00],
                    "Musk, Elon": [1000000.00, 30000.00],
                    "Zuckerberg, Mark": [10000.00, 50000.00, 2000.00, 400000.00]
                    }
    assert mr.add_donor("Mann, Rusty", 100) == {"Allen, Paul": [1000000.00, 50000.00, 300000.00, 10], 
                    "Gates, Bill": [5000000.00, 80000.00, 700000.00], 
                    "Bezos, Jeff": [30000.00], 
                    "Musk, Elon": [1000000.00, 30000.00], 
                    "Zuckerberg, Mark": [10000.00, 50000.00, 2000.00, 400000.00],
                    "Mann, Rusty": [100]}

#def test_donor_selection():
    #with "mann, rusty" passed as input
    #assert mr.donor_selection() == "Mann, Rusty"
    #with "allen paul" passed as input
    #assert mr.donor_selection() == "Allen Paul"


def test_get_donor_name():
    #with "Menu" passed as input
    #assert mr.get_donor_name() == None
    #with "LIST " passed as input
    assert mr.get_donor_name() == print(["Allen, Paul",
     "Bezos, Jeff", "Gates, Bill", "Musk, Elon", "Zuckerberg, Mark"])
    #assert mr.get_donor_name() is True
