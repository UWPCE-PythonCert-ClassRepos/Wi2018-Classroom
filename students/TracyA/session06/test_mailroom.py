#!/usr/bin/env python

import mailroom_session06 as ta
import os


def test_1():
    assert ta.show_list() == print(["Allen, Paul",
                                    "Bezos, Jeff",
                                    "Gates, Bill",
                                    "Musk, Elon",
                                    "Zuckerberg, Mark"])


def get_donor():
    assert ta.get_donor("Allen, Paul") == "Allen, Paul"


def test_no_donor_found():
    assert ta.get_donor("Allen, Tracy") is None


def test_split_name():
    assert ta.split_name("Gates, Bill") == ('Bill', 'Gates')


def test_donor_dict():
    assert ta.make_donor_dict("Allen, Paul", 10.0) == {
        "first name": "Paul", "last name": "Allen", "amt": 10.0}


def test_add_donor():
    ta.add_donor("Flinstone, Fred", 10) == {"Flinstone, Fred": [10]}


def test_make_report():
    report = ta.make_report()

    print(report)
    assert report.startswith("Donor Name           | Total Given | Num Gifts       | Average Gift")
    assert "Gates, Bill         $     5780000.00       3       $  1926666.67" in report


def test_save_letter_files():
    """
    This only tests that the files get created.
    """
    ta.create_letter_files()

    assert os.path.isfile('Allen_Paul.txt')
    assert os.path.isfile('Gates_Bill.txt')
    # check that it's not empty
    with open('Gates_Bill.txt') as f:
        size = len(f.read())
    assert size > 0
