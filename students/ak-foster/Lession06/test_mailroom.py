#!/usr/bin/env python3
from mailroom4 import *

def test_1():
    assert thankYouNote('Name', '100') == "Name,\n\nThank you for your gift of 100 dollars. Your donation will be put to good use.\n\n - The Team"


def test_2():
    recordDonation('Ed', 1000)
    assert 'Ed' in donate
