#!/usr/bin/env python3

"""
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/mailroom.html#exercise-mailroom-testing

Add unit tests for mailroom.py -- using pytest
"""
import mailroom as mr

def test_clear_db():
    mr.add_donation("alpha", 100)
    mr.clear_db()
    assert(not any(mr.get_db()))

def test_build_thankyou():
    mr.clear_db()
    mr.add_donation("alpha", 100)
    assert(mr.build_thankyou("alpha") == "Thank you, alpha, for your donation(s) of $100!\n")


def test_add_donation():
    mr.clear_db()
    mr.add_donation("alpha", 100)
    assert(mr.get_db()["alpha"] == [100])


def test_generate_stats():
    mr.clear_db()
    mr.add_donation("alpha", 100)
    total, number, average = mr.generate_stats("alpha")
    assert(total == 100 and number == 1 and average == 100)
    mr.add_donation("alpha", 200)
    total, number, average = mr.generate_stats("alpha")
    assert(total == 300 and number == 2 and average == 150)


