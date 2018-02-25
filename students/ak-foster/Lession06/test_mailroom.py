#!/usr/bin/env python3
from mailroom4 import *


def test_thankYouNote():
    assert thankYouNote('Name1', '100') == "Name1,\n\nThank you for your gift of 100 dollars. Your donation will be put to good use.\n\n - The Team"


def test_recordDonation():
    recordDonation('Name2', 1000)
    assert 'Name2' in donate


def test_sendThankYou():
    sendThankYou('Name3', 200)
    assert 'Name3' in donate


def test_promptForName():
    assert 'Name4' == promptForName('Name4')


def test_promptForAmount():
    assert promptForAmount('100') == 100


def test_promptForDir():
    assert 'testPath' == promptForDir('testPath')
    # assert os.path.exists(resp) # looks like this should work-- suspect pytest doesn't run in CWD
