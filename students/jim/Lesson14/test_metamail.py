import metamail as mm

db = mm.DonorDatabase()

def test_init():
    # Test that instances initialize correctly
    assert db.data == {}

def test_new_donor():
    # Test adding a new donor to the database object
    db.new_donor('Genghis Khan')
    assert 'Genghis Khan' in db.data.keys()
    assert db.data['Genghis Khan'] == []

def test_new_donation():
    db.new_donation('Genghis Khan', 25)
    assert db.data['Genghis Khan'] == [25]