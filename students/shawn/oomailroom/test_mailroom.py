from mailroom import Donor,Donors,Stat
import pytest


@pytest.fixture
def d():
    dl=Donors();
    dl.load("data.csv")
    return Donor("Bobby","Orr",[50,100,150]),dl

def test_donor_init():
    assert d()[0].fnam == "Bobby" and d()[0].lnam == "Orr" and int(sum(d()[0].donation) == 300)

def test_donor_str():
    assert d()[0].__str__().startswith("<p>")

def test_iadd():
    donor = d()[0]
    donor += 100
    assert int(sum(donor.donation))==400

def test_add_donation():
    donor = d()[0]
    donor.add_donation(100)
    assert sum(donor.donation) == 400
    donor.add_donation([50,50])
    assert sum(donor.donation) == 500
    donor.add_donation((50,50))
    assert sum(donor.donation) == 600

def test_get_stat():
    donor=d()[0]
    assert donor.get_stats(Stat.x) == "100.00"
    assert donor.get_stats(Stat.s) == "300.00"
    assert donor.get_stats(Stat.n) == "3"

def test_keyval():
    assert  d()[0].keyval == "bobbyorr"

def test_make_key():
    assert Donor.make_key("Usey Von Username") == "useyvonusername"


