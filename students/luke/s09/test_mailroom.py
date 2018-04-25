#!/usr/bin/env python3

"""
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/mailroom.html#exercise-mailroom-testing

Add unit tests for mailroom.py -- using pytest
"""
from mailroom import DonorList as dl

def test_clear_db():
    mr = dl()
    mr.add_donation("alpha", 100)
    mr.clear_db()
    assert(not mr.get_donors().get("alpha"))

test_clear_db()

def test_build_thankyou():
    mr = dl()
    mr.clear_db()
    mr.add_donation("alpha", 100)
    assert(mr.build_thankyou("alpha") == "Thank you, alpha, for your donation(s) of $100!\n")


test_build_thankyou()

def test_add_donation():
    mr = dl()
    mr.clear_db()
    mr.add_donation("alpha", 100)
    assert(mr.donors["alpha"].donations == [100])


def test_generate_stats():
    mr = dl()
    mr.clear_db()
    mr.add_donation("alpha", 100)
    total, number, average = mr.generate_stats("alpha")
    assert(total == 100 and number == 1 and average == 100)
    mr.add_donation("alpha", 200)
    total, number, average = mr.generate_stats("alpha")
    assert(total == 300 and number == 2 and average == 150)


