from donor_classes import Donor, DonorCollection
import math
import pytest

@pytest.fixture
def my_donor():
	return Donor("Jon", "Smith", 4.00)

@pytest.fixture
def my_collection():
	return DonorCollection()

def test_get_full_name(my_donor):
	new_name = my_donor.get_full_name()
	assert new_name == "Jon Smith"

def test_append_donation(my_donor):
	my_donor.append_donation(5.00)
	assert my_donor.donation_list == [4.00, 5.00]

def test_thank_you_message(my_donor):
	thank_you = my_donor.thank_you_letter()
	assert "Thank you Jon Smith" in thank_you
	assert "4.00" in thank_you

def test_num_donations(my_donor):
	assert my_donor.num_donations == 1

def test_sum_donations(my_donor):
	assert my_donor.sum_donations == 4.00

def test_avg_donations(my_donor):
	assert my_donor.avg_donations == 4.00

def test_clean_text(my_collection):
	test_str = "teSt "
	assert my_collection.clean_text(test_str) == "Test"

def test_create_dict_key(my_collection):
	first = "Jon"
	last = "Smith"
	assert my_collection.create_dict_key(first, last) == ("Jon", "Smith")

def test_write_file(my_collection):
	with open("Navdeep_Gill.txt") as f:
		size = len(f.read())
	assert size > 0

def test_report_header(my_collection):
	assert "Donor Name" in my_collection.report_header()
	assert "Num Gifts" in my_collection.report_header()

def test_append_dict(my_collection):
	new_donor = Donor("Navdeep", "Gill", 1000)
	my_collection.append_collection_dict(new_donor)
	for element in my_collection.donor_dict.values():
		assert element.get_full_name() == 'Navdeep Gill'
		assert element.num_donations == 1
		assert element.avg_donations == 1000.00

def test_create_report(my_collection):
	new_donor = Donor("Navdeep", "Gill", 1000)
	my_collection.append_collection_dict(new_donor)
	assert "Navdeep Gill" in my_collection.create_report()
	assert "1000" in my_collection.create_report()

def test_letter_to_file(my_collection):
	assert "Jon Smith" in my_collection.letter_to_file("Jon Smith", 40)

def test_donor_exists(my_collection, my_donor):
	first = "Jon"
	last = "Smith"
	my_collection.append_collection_dict(my_donor)
	assert my_collection.donor_exists(first, last) == True
