#!/usr/bin/env python3
"""
pytest for mailroom 4.

"""
# Since I wrote mailroom4, I'm ok w/ importing *
from mailroom4 import * 
import pathlib

def test_pick_ty_recipient00():
    assert pick_ty_recipient("bob") == "Bob"


def test_pick_ty_recipient01():
    assert pick_ty_recipient("jIM") == "Jim"


def test_thank_you_txt00():
    assert thank_you_txt("Beth") == "Dear Beth,\n\n \tThanks so much for your generous\
 donations totaling $31245.75.\n \tWe are\
 all incredibly grateful because blah blah. \n\n-NGO"


def test_send_ty00():
    # I'm not sure how to test input() options with pytest?
    assert send_ty("Ann") == thank_you_txt("Ann")


def test_generate_report00():
    # Checking part, because formatting == tedious
    assert generate_report()[:17] == "Donor Name      |"


def test_generate_report01():
    # Checking another part
    assert generate_report()[83:87] == "5.87"


def test_send_letters00():
    # okay, this one is stupid.
    assert send_letters() == "sent!"


def test_send_letters01():
    # Check if there are the correct number of letters
    assert len([f for f in pathlib.Path('./letters').iterdir()]) == len(donors)


def test_send_letters02():
    # Check the contents of one of the letters.
    with open("letters/Bob.txt") as f:
        assert f.read() == "Dear Bob,\n\n \tThanks so much for your generous\
 donations totaling $67.86.\n \tWe are\
 all incredibly grateful because blah blah. \n\n-NGO"


def test_mailroom00():
    # Other functions above, so testing if 4 returns nothing.
    # Not sure how to test input() in while loop w/ pytest?
    assert mailroom("4") == None
