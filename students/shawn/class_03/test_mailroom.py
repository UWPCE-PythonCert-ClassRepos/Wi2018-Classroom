from mailroom import Donor ,Donors


#-----------------------------------------------------------------------*
# Test Donor and Donors methods
#-----------------------------------------------------------------------*
donor=Donor("Bobby","Orr",50)
donor_list = Donors()
donor_list.load_default()

def test_load_default():
    assert len(donor_list.donors) > 0

def test_donor_str():
    """ Test the attributes of the donor class"""
    expected=['add_donation','donation','fnam','lnam','keyval']
    attr=[i for i in dir(donor) if not i.startswith('__')]
    assert set(attr).difference(expected).__len__()==0

def test_donor_constructor():
    d=Donor("Shawn","Hopkins",100)
    assert d.fnam=='Shawn'
    assert d.lnam=='Hopkins'
    assert sum(d.donation)==100

def test_add_donation():
    d1 = Donor("Shawn", "Hopkins",100)
    d1.add_donation(100)
    assert sum(d1.donation) ==200

def test_keyval():
    d1 = Donor("Shawn", "Hopkins", 100)
    assert d1.keyval== d1.fnam.lower() + d1.lnam.lower()

def test_get_or_create():
    d1=Donor("bob", "jones", 100)
    assert donor_list.get_or_create(d1)[1] is True
    d=Donor("Bill", "Buckner", 100)
    assert donor_list.get_or_create(d)[1] is False

def test_get():
    assert donor_list.get("billbuckner")[0] is True
    assert donor_list.get("hamflake")[0] is False

def test_report():
    assert donor_list.report() != None

def test_read_data():
    t1=donor_list.read_data("Shawn","Hopkins",50)
    assert t1[0] is True
    assert t1[1].keyval=='shawnhopkins'
    t2=donor_list.read_data("Bill","Buckner",100000)
    assert t2[0] is False
    assert sum(t2[1].donation) > 100000





