#!/usr/bin/env python 3


############################
## 
## test_Mailroom_4.py

import unittest
import MailRoom_4 

from MailRoom_4 import *


def test_createReportData():
	assert createReportData(True) == [[5100.0, 'Barak_Obama', 3, 1700.0], [3300.0, 'Peter_Piper', 3, 1100.0], [3100.0, 'Bill_Gates', 3, 1033.0], [3000.5, 'Mary_Poppins', 2, 1500.0], [300.0, 'Lucille_Ball', 2, 150.0]]


def test_findDonorName():
	assert "newDonor" == findDonorName("newDonor")


def test_retrieveDonationAmount():
	assert retrieveDonationAmount('John Doe', 100) == 100


def test_printLetter():
    assert printLetter('Barak Obama', 100) == "\nDear Barak Obama,\nThank you for your donation of $100.\nSincerely,\nThe Team\n"


def test_recordDonation():
    recordDonation('Mr. Rogers', 100)
    assert 'Mr. Rogers' in donorDict
"""
def test_printReportData(): 
##how would I test is specified correctly? seems like a visual check is the best. 

def test_sendLettersToAll():#
#This is just a bunch of print statements written to current directory to test?
would I open each one and make sure it has proper text?	

def test_printThankYouLetter():
##This function in my code just calls other functions. How to test?
"""
