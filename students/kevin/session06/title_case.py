# test_case.py

def title_case(x):
    if not isinstance(x, str):
        raise TypeError('Please provide a string argument')
    return x.title()

def test_title_case():
    assert title_case('lady gaga') == 'Lady Gaga'

def test_string():
    with pytest.raises(TypeError):
        title_case(9)
